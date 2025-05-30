import os
from estat_python_adapter import EstatConnector  # 正しいモジュールパスに修正

def main():
    # 1. APIキーを環境変数から取得
    api_key = os.environ.get("ESTAT_API_KEY")
    if not api_key:
        raise RuntimeError("ESTAT_API_KEY 環境変数がセットされていません")

    # 2. コネクタ生成
    estat = EstatConnector(api_key=api_key)

    # 3. 帳票（統計表）検索：キーワード例「人口」で
    df_stats = estat.search_stats(searchWord="人口", limit=10)
    print(df_stats[["id", "STAT_NAME", "TITLE"]])  # 主要項目だけ表示

if __name__ == "__main__":
    main()