import requests
import pandas as pd
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

        # id属性を含めたい場合
        for t in table_infs:
            if "@id" in t:
                t["id"] = t["@id"]
        return pd.json_normalize(table_infs)

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
            rec["value"] = rec.pop("$", None)
            records.append(rec)
        return pd.DataFrame(records)


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
