# e-Stat Python アダプターの使い方

このライブラリは、e-Stat APIを簡単に利用するためのPythonアダプターです。

## 1. 基本的な使い方

### インスタンスの作成

まず、`EstatConnector`クラスのインスタンスを作成します。APIキーが必要です。

```python
from estat_python_adapter import EstatConnector

# APIキーを設定
API_KEY = "あなたのAPIキー"  # 実際のAPIキーに置き換えてください
estat = EstatConnector(api_key=API_KEY)
```

### パラメータ

インスタンス生成時に指定できるパラメータ:
- `api_key`: e-Stat APIのアプリケーションID（必須）
- `version`: APIバージョン（デフォルト: "3.0"）
- `lang`: 言語設定（デフォルト: "J"（日本語）、"E"（英語）も指定可能）

## 2. 統計表情報の検索

`search_stats`メソッドを使用して、統計表を検索できます。

```python
# キーワード「人口」で統計表を検索
stats_df = estat.search_stats(searchWord="人口", limit=10)
stats_df.head()

# 特定の統計分野で検索 (例: 03=労働・賃金)
labor_stats = estat.search_stats(statsField="03", limit=5)

# 統計表コードで直接検索
specific_stats = estat.search_stats(statsCode="00200", limit=5)

# 調査年で検索
yearly_stats = estat.search_stats(surveyYears="2020", limit=5)
```

### 主なパラメータ

- `searchWord`: キーワード検索（例: "東京 AND 人口"）
- `statsField`: 統計分野（例: "03"（労働・賃金））
- `statsCode`: 政府統計コード
- `surveyYears`: 調査年月（例: "2020"、"202001"、"202001-202012"）
- `limit`: 取得件数（デフォルト: 1000）
- `startPosition`: データ取得開始位置（デフォルト: 1）

## 3. 統計データの取得

`get_stats_data`メソッドを使用して、特定の統計表のデータを取得できます。

```python
# 検索結果から最初の統計表IDを取得
if not stats_df.empty:
    stats_id = stats_df.iloc[0]['id']
    print(f"統計表ID: {stats_id}")
    
    # 統計データを取得
    stats_data = estat.get_stats_data(statsDataId=stats_id)
    stats_data.head()
```

### データ絞り込み

特定の条件でデータを絞り込むことができます。

```python
# 特定の統計表IDを直接指定してデータ取得（限定条件付き）
filtered_data = estat.get_stats_data(
    statsDataId="0003348423",  # 実際の統計表IDに置き換え
    startPosition=1,
    limit=1000,
    # 以下は必要に応じて使用（統計表によって利用可能なパラメータが異なります）
    # cdCat01="10001",  # カテゴリ1のコード
    # cdArea="01000"    # 地域コード
)
```

### 主なパラメータ

- `statsDataId`: 統計表ID（必須、`dataSetId`との排他的選択）
- `dataSetId`: データセットID（必須、`statsDataId`との排他的選択）
- `lvTab`: 表章事項の階層レベル
- `cdTab`: 表章事項のコード
- `cdArea`: 地域コード
- `cdTime`: 時間軸コード
- `cdCat01`～`cdCat15`: 分類事項コード（01～15まで）
- `startPosition`: データ取得開始位置（デフォルト: 1）
- `limit`: 取得件数（デフォルト: 100000）

## 4. 取得したデータの加工例

```python
# データが存在する場合
if not stats_data.empty:
    # 数値型に変換
    stats_data['value'] = pd.to_numeric(stats_data['value'], errors='coerce')
    
    # 基本的な統計情報
    stats_data['value'].describe()
    
    # 特定の条件でフィルタリング
    filtered = stats_data[stats_data['@area'] == '全国']
```

## 5. エラーハンドリング

APIからエラーが返された場合、`EstatAPIError`例外が発生します。

```python
from estat_python_adapter import EstatConnector, EstatAPIError

try:
    stats_data = estat.get_stats_data(statsDataId="不正なID")
except EstatAPIError as e:
    print(f"APIエラー: {e}")
```

## 参考リンク

- [e-Stat API 機能説明](https://www.e-stat.go.jp/api/api-info/api-spec)
- [e-Stat API リファレンス](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0) 