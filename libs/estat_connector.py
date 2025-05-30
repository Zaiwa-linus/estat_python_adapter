import requests
import pandas as pd
import re
from typing import Optional, Dict, Any, Union, List


class EstatAPIError(Exception):
    """e-Stat APIからエラーが返却された場合の例外"""
    pass


class EstatConnector:
    BASE_URL = "https://api.e-stat.go.jp/rest"
    DEFAULT_VERSION = "3.0"

    def __init__(self, api_key: str, version: str = DEFAULT_VERSION, lang: str = "J"):
        self.api_key = api_key
        self.version = version
        self.lang = lang

    def _request(self, endpoint: str, params: Dict[str, Any], method: str = "GET") -> Dict[str, Any]:
        # APIキー・バージョン・言語パラメータ付与
        params = params.copy()
        params["appId"] = self.api_key
        params["lang"] = self.lang

        url = f"{self.BASE_URL}/{self.version}/app/json/{endpoint}"
        resp = requests.get(url, params=params) if method == "GET" else requests.post(url, data=params)
        resp.raise_for_status()
        data = resp.json()
        # 共通: エラー判定
        result = data.get("RESULT") or data.get("result") or {}
        status = int(result.get("STATUS", 0))
        if status != 0:
            msg = result.get("ERROR_MSG", "Unknown Error")
            raise EstatAPIError(f"API Error: STATUS={status}, MSG={msg}")
        return data

    def _normalize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """列名から@、$などの記号を除去し、正規化する"""
        renamed_columns = {}
        for col in df.columns:
            # @で始まる属性名を正規化
            if col.startswith('@'):
                renamed_columns[col] = col[1:]
            # $はvalueに変換
            elif col == '$':
                renamed_columns[col] = 'value'
            # 一般的なケースでアンダースコアに置換
            elif re.search(r'[^a-zA-Z0-9_]', col):
                new_name = re.sub(r'[^a-zA-Z0-9_]', '_', col)
                # 連続したアンダースコアを一つに
                new_name = re.sub(r'_{2,}', '_', new_name)
                # 末尾のアンダースコアを削除
                new_name = new_name.rstrip('_')
                renamed_columns[col] = new_name
                
        return df.rename(columns=renamed_columns)

    def search_stats(
        self,
        searchWord: Optional[str] = None,
        statsField: Optional[str] = None,
        statsCode: Optional[str] = None,
        surveyYears: Optional[str] = None,
        limit: int = 1000,
        **kwargs
    ) -> pd.DataFrame:
        """
        統計表情報（帳票）の検索
        """
        params = {
            "limit": limit,
        }
        if searchWord: params["searchWord"] = searchWord
        if statsField: params["statsField"] = statsField
        if statsCode: params["statsCode"] = statsCode
        if surveyYears: params["surveyYears"] = surveyYears
        params.update(kwargs)

        data = self._request("getStatsList", params)
        # データ部抽出
        datalist_inf = (data.get("GET_STATS_LIST") or {}).get("DATALIST_INF", {})
        table_infs = datalist_inf.get("TABLE_INF", [])
        # 単数の場合もリスト化
        if isinstance(table_infs, dict):
            table_infs = [table_infs]
        if not table_infs:
            return pd.DataFrame()  # 空DataFrame

        # 属性を持つ要素の正規化（@idの手動変換は不要）
        for t in table_infs:
            # 属性を持つ要素の正規化
            for key, value in list(t.items()):
                if isinstance(value, dict) and "@code" in value:
                    # 属性と値を別々の列に分ける
                    code_value = value.get("@code")
                    text_value = value.get("$")
                    
                    # コード列を追加
                    if code_value is not None:
                        t[f"{key}_code"] = code_value
                    
                    # 元の列をテキスト値で置き換え
                    if text_value is not None:
                        t[key] = text_value
                    # テキスト値がなければ属性値を使用
                    elif code_value is not None:
                        t[key] = code_value
        
        df = pd.json_normalize(table_infs)
        # 列名の正規化
        return self._normalize_column_names(df)

    def get_stats_data(
        self,
        statsDataId: Optional[str] = None,
        dataSetId: Optional[str] = None,
        lvTab: Optional[str] = None,
        cdTab: Optional[str] = None,
        startPosition: int = 1,
        limit: int = 100000,
        **kwargs
    ) -> pd.DataFrame:
        """
        統計データ取得
        """
        assert statsDataId or dataSetId, "statsDataIdかdataSetIdのどちらか必須"
        params = {
            "startPosition": startPosition,
            "limit": limit,
        }
        if statsDataId: params["statsDataId"] = statsDataId
        if dataSetId: params["dataSetId"] = dataSetId
        if lvTab: params["lvTab"] = lvTab
        if cdTab: params["cdTab"] = cdTab
        params.update(kwargs)

        data = self._request("getStatsData", params)
        # データ部抽出
        sdata = (data.get("GET_STATS_DATA") or {}).get("STATISTICAL_DATA", {})
        datainf = sdata.get("DATA_INF", {})
        values = datainf.get("VALUE", [])
        if isinstance(values, dict):
            values = [values]
        if not values:
            return pd.DataFrame()
        # 属性＋値でDataFrame化
        records = []
        for v in values:
            rec = v.copy()
            # "$" キーがある場合は "value" に変換
            if "$" in rec:
                rec["value"] = rec.pop("$", None)
            records.append(rec)
        df = pd.DataFrame(records)
        # 列名の正規化
        return self._normalize_column_names(df)


# 例：利用方法
if __name__ == "__main__":
    # app_idは利用者が登録して取得
    estat = EstatConnector(api_key="YOUR_ESTAT_APP_ID")
    
    # 統計表をキーワードで検索
    df_stats = estat.search_stats(searchWord="人口")
    print(df_stats.head())
    
    # 具体的な統計表IDでデータを取得
    # statsDataIdはdf_stats['id']などで得られる
    if not df_stats.empty:
        stats_id = df_stats.iloc[0]['id']
        df_data = estat.get_stats_data(statsDataId=stats_id)
        print(df_data.head())
