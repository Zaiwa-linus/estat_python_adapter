# estat_python_adapter
e-Statのデータを取得するための非公式Pythonライブラリです。

## 概要

このプロジェクトは、[e-Stat API](https://www.e-stat.go.jp/api/)を簡単に利用するためのPythonアダプターを提供します。e-Statは日本の政府統計ポータルサイトで、様々な統計データにアクセスできます。

## インストール

### pip経由でのインストール

```bash
pip install git+https://github.com/Zaiwa-linus/estat_python_adapter.git
```

### ソースからのインストール

```bash
git clone https://github.com/Zaiwa-linus/estat_python_adapter.git
cd estat_python_adapter
pip install -e .
```

## 使い方

基本的な使い方は以下の通りです：

```python
from estat_python_adapter import EstatConnector

# APIキーを設定（e-Statサイトで取得したアプリケーションID）
API_KEY = "あなたのAPIキー"
estat = EstatConnector(api_key=API_KEY)

# 統計表の検索
stats_df = estat.search_stats(searchWord="人口")

# 統計データの取得
if not stats_df.empty:
    stats_id = stats_df.iloc[0]['id']
    stats_data = estat.get_stats_data(statsDataId=stats_id)
```

詳細な使用例は以下のファイルを参照してください：
- [使用方法ガイド](lab/sample_usage.md)
- [サンプルコード](lab/example.py)

## サポートしている機能

- 統計表情報（帳票）の検索
- 統計データの取得

## ライセンス

MITライセンス

## 参考リンク

- [e-Stat API 機能説明](https://www.e-stat.go.jp/api/api-info/api-spec)
- [e-Stat API リファレンス](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0)


