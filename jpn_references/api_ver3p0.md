## 目次

1. API機能の種類
2. APIの利用方法
   - 2.1 統計表情報取得
   - 2.2 メタ情報取得
   - 2.3 統計データ取得
   - 2.4 データセット登録
   - 2.5 データセット参照
   - 2.6 データカタログ情報取得
   - 2.7 統計データ一括取得
3. APIパラメータ
   - 3.1 全API共通
   - 3.2 統計表情報取得
   - 3.3 メタ情報取得
   - 3.4 統計データ取得
   - 3.5 データセット登録
   - 3.6 データセット参照
   - 3.7 データカタログ情報取得
   - 3.8 統計データ一括取得
4. APIの出力データ
   - 4.1 全API共通
   - 4.2 統計表情報取得
   - 4.3 メタ情報取得
   - 4.4 統計データ取得
   - 4.5 データセット登録
   - 4.6 データセット参照
   - 4.7 データカタログ情報取得
   - 4.8 統計データ一括取得


## 2. APIの利用方法

e-Statの各APIは、指定されたURLに対してリクエストを送信することで利用できます。リクエスト形式には XML、JSON、JSONP、CSV があり、HTTPSにも対応しています。

アプリケーションID（appId）の指定が必須です。利用には事前登録が必要です。

---

### 2.1 統計表情報取得

- **HTTPメソッド**：GET

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getStatsList?<パラメータ群>`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/getStatsList?<パラメータ群>`
- JSONP: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/jsonp/getStatsList?<パラメータ群>`
- CSV: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getSimpleStatsList?<パラメータ群>`

---

### 2.2 メタ情報取得

- **HTTPメソッド**：GET

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getMetaInfo?<パラメータ群>`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/getMetaInfo?<パラメータ群>`
- JSONP: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/jsonp/getMetaInfo?<パラメータ群>`
- CSV: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getSimpleMetaInfo?<パラメータ群>`

---

### 2.3 統計データ取得

- **HTTPメソッド**：GET

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getStatsData?<パラメータ群>`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/getStatsData?<パラメータ群>`
- JSONP: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/jsonp/getStatsData?<パラメータ群>`
- CSV: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getSimpleStatsData?<パラメータ群>`

---

### 2.4 データセット登録

- **HTTPメソッド**：POST  
- **Content-Type**：`application/x-www-form-urlencoded`

#### リクエストURL形式：
- `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/postDataset`

※POSTリクエストのため、HTTPヘッダーにContent-Typeの指定が必要です。

---

### 2.5 データセット参照

- **HTTPメソッド**：GET

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/refDataset?<パラメータ群>`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/refDataset?<パラメータ群>`
- JSONP: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/jsonp/refDataset?<パラメータ群>`

---

### 2.6 データカタログ情報取得

- **HTTPメソッド**：GET

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getDataCatalog?<パラメータ群>`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/getDataCatalog?<パラメータ群>`
- JSONP: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/jsonp/getDataCatalog?<パラメータ群>`

---

### 2.7 統計データ一括取得

- **HTTPメソッド**：POST

#### リクエストURL形式：
- XML: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getStatsDatas`
- JSON: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/json/getStatsDatas`
- CSV: `http(s)://api.e-stat.go.jp/rest/<バージョン>/app/getSimpleStatsDatas`


## 3. APIパラメータ

APIリクエスト時には、目的に応じたパラメータを設定する必要があります。  
GETメソッドの場合はURLにクエリとして付加し、POSTの場合はリクエストボディに指定します。  
文字コードは UTF-8 で URLエンコードしてください。

---

### 3.1 全API共通

| パラメータ名 | 意味              | 必須 | 設定内容 |
|--------------|-------------------|------|----------|
| appId        | アプリケーションID | ○   | 利用登録で取得したID |
| lang         | 言語              | -    | `J`：日本語（デフォルト）、`E`：英語 |

---

### 3.2 統計表情報取得

| パラメータ名         | 意味                 | 必須 | 設定内容例 |
|----------------------|----------------------|------|------------|
| surveyYears          | 調査年月             | -    | `yyyy`、`yyyymm`、`yyyymm-yyyymm` |
| openYears            | 公開年月             | -    | 同上 |
| statsField           | 統計分野             | -    | `03`（労働・賃金など） |
| statsCode            | 政府統計コード       | -    | `00200`（作成機関など） |
| searchWord           | キーワード検索       | -    | `東京 AND 人口` など |
| searchKind           | データ種別           | -    | `1`：統計情報、`2`：小地域・地域メッシュ |
| collectArea          | 集計地域区分         | -    | `1`：全国、`2`：都道府県、`3`：市区町村 |
| explanationGetFlg    | 解説取得フラグ       | -    | `Y`（デフォルト） / `N` |
| statsNameList        | 調査名一覧取得フラグ | -    | `Y`：調査名一覧取得 |
| startPosition        | データ取得開始位置   | -    | `1`（初期値） |
| limit                | 取得件数             | -    | デフォルト：100,000件 |
| updatedDate          | 更新日付指定         | -    | `yyyy` / `yyyymmdd-yyyymmdd` |
| callback             | JSONP用関数名        | △   | JSONP形式でのみ必須 |

---

### 3.3 メタ情報取得

| パラメータ名       | 意味             | 必須 | 設定内容例 |
|--------------------|------------------|------|------------|
| statsDataId        | 統計表ID         | ○   | `0003084821` など |
| explanationGetFlg  | 解説取得フラグ   | -    | `Y`（デフォルト） / `N` |
| callback           | JSONP用関数名    | △   | JSONP形式でのみ必須 |

---

### 3.4 統計データ取得

| パラメータ名         | 意味                     | 必須 | 補足 |
|----------------------|--------------------------|------|------|
| dataSetId            | データセットID           | △    | `statsDataId`とどちらか必須 |
| statsDataId          | 統計表ID                 | △    | 同上 |
| lvTab                | 表章事項の階層レベル     | -    | `1-3` など範囲指定可能 |
| cdTab                | 単一コード（項目コード） | -    | カンマ区切りで最大100個 |
| cdTabFrom / To       | コード範囲指定           | -    | From-To指定可 |
| lvTime / cdTime      | 時間軸階層/コード        | -    | メタ情報に準拠 |
| lvArea / cdArea      | 地域階層/コード          | -    | 同上 |
| lvCat01 ~ lvCat15    | 分類事項階層/コード      | -    | 最大15分類まで対応 |
| startPosition        | 開始位置                 | -    | `1`（デフォルト） |
| limit                | 取得件数                 | -    | 最大100,000件 |
| metaGetFlg           | メタ情報取得フラグ       | -    | `Y`（デフォルト） / `N` |
| cntGetFlg            | 件数のみ取得フラグ       | -    | `Y`：件数のみ / `N`（デフォルト） |
| explanationGetFlg    | 解説取得フラグ           | -    | `Y` / `N` |
| annotationGetFlg     | 注釈情報取得フラグ       | -    | `Y` / `N` |
| replaceSpChars       | 特殊文字置換             | -    | `0`〜`3`（例：`1`=0に置換） |
| sectionHeaderFlg     | セクションヘッダ出力     | -    | `1`：出力（デフォルト）/ `2`：なし |
| callback             | JSONP関数名              | △   | JSONP形式のみ必須 |

---

### 3.5 データセット登録

- `POST`メソッド使用、Content-Typeは `application/x-www-form-urlencoded`

| パラメータ名         | 意味                     | 必須 | 備考 |
|----------------------|--------------------------|------|------|
| dataSetId            | データセットID           | △    | 未指定時は自動生成される |
| statsDataId          | 統計表ID                 | △    | `E`モード時に必須 |
| lvTab ~ lvCatXX      | 各絞り込み条件           | △    | 複数条件をANDで指定可能 |
| openSpecified        | 公開設定                 | -    | `0`：非公開（初期値）、`1`：公開 |
| processMode          | 処理モード               | -    | `E`：登録・更新、`D`：削除 |
| dataSetName          | データセット名           | -    | 256文字まで指定可 |

---

### 3.6 データセット参照

| パラメータ名        | 意味            | 必須 | 備考 |
|---------------------|-----------------|------|------|
| dataSetId           | データセットID  | -    | 未指定時はすべてを一覧取得 |
| collectArea         | 集計地域区分    | -    | `1`：全国など（dataSetId指定時は無効） |
| explanationGetFlg   | 解説取得        | -    | `Y` / `N`（デフォルト） |
| callback            | JSONP関数名     | △   | JSONP形式のみ必須 |

---

### 3.7 データカタログ情報取得

| パラメータ名       | 意味                 | 必須 | 備考 |
|--------------------|----------------------|------|------|
| surveyYears        | 調査年月             | -    | yyyy / yyyymm / 範囲など |
| openYears          | 公開年月             | -    | 同上 |
| statsField         | 統計分野             | -    | 数値コード |
| statsCode          | 政府統計コード       | -    | 作成機関 or 統計コード |
| searchWord         | 検索キーワード       | -    | AND / OR / NOT 対応 |
| collectArea        | 集計地域区分         | -    | 全国/都道府県など |
| explanationGetFlg  | 解説情報取得         | -    | `Y`（デフォルト）/ `N` |
| dataType           | ファイル形式指定     | -    | `XLS`, `CSV`, `PDF`, `DB`等 |
| catalogId          | カタログID           | -    | 任意のID |
| resourceId         | カタログリソースID   | -    | 任意のID |
| startPosition      | 開始位置             | -    | `1`（デフォルト） |
| limit              | 件数                 | -    | デフォルト：100 |
| updatedDate        | 更新日付             | -    | 日付/範囲 |
| callback           | JSONP関数名          | △   | JSONP形式のみ必須 |

---

### 3.8 統計データ一括取得

複数の統計表IDまたはデータセットIDに対応する統計データ（数値）を一括で取得するAPIです。  
HTTPメソッドは **POST** で、リクエストパラメータは JSON 形式の文字列として送信します。

---

#### パラメータ一覧

| パラメータ名           | 意味                     | 必須 | 設定内容・備考 |
|------------------------|--------------------------|------|----------------|
| metaGetFlg             | メタ情報取得有無         | -    | `Y`（取得する、デフォルト） / `N`（取得しない）<br>※CSV形式では無効（常に `N`） |
| explanationGetFlg      | 解説情報取得有無         | -    | `Y`（取得する、デフォルト） / `N`（取得しない） |
| annotationGetFlg       | 注釈情報取得有無         | -    | `Y`（取得する、デフォルト） / `N`（取得しない） |
| replaceSpChars         | 特殊文字の置換           | -    | - `0`（置換しない、デフォルト）<br> - `1`（0に置換）<br> - `2`（空文字に置換）<br> - `3`（文字列NAに置換） |
| sectionHeaderFlg       | セクションヘッダ出力     | -    | CSV形式のときのみ有効<br> - `1`（出力する、デフォルト）<br> - `2`（出力しない） |
| statsDatasSpec         | 統計データ一括取得パラメータリスト | ○ | JSON形式で定義されたリクエストの配列。<br>各リクエストには以下の指定が可能。 |

---

#### statsDatasSpec の構造（JSON形式）

一括で取得する統計データIDと、必要に応じた絞り込み条件を指定します。

```json
[
  {
    "statsDataId": "0003084821",
    "lvTab": "1-2",
    "cdCat01": "01"
  },
  {
    "statsDataId": "0005084822",
    "cdAreaFrom": "01000",
    "cdAreaTo": "02000"
  },
  {
    "statsDataId": "0005084823",
    "cdAreaFrom": "02000",
    "cdAreaTo": "02000"
  }
]
```

---

#### 各リクエストに指定可能なパラメータ

| パラメータ名     | 意味                         | 必須 | 備考 |
|------------------|------------------------------|------|------|
| dataSetId        | データセットID               | △    | `statsDataId`とどちらかは必須 |
| statsDataId      | 統計表ID                     | △    | 同上 |
| lvTab            | 表章事項 階層レベル          | -    | 例：`1`、`1-3`、`-2`、`4-` |
| cdTab            | 表章事項 単一コード          | -    | カンマ区切りで最大100個まで指定可 |
| cdTabFrom        | 表章事項 コード From         | -    | 範囲の開始コード |
| cdTabTo          | 表章事項 コード To           | -    | 範囲の終了コード |
| lvTime           | 時間軸事項 階層レベル        | -    | 同様に階層で絞り込み |
| cdTime           | 時間軸事項 単一コード        | -    | 時間コード指定 |
| cdTimeFrom       | 時間軸事項 コード From       | -    | 範囲の開始コード |
| cdTimeTo         | 時間軸事項 コード To         | -    | 範囲の終了コード |
| lvArea           | 地域事項 階層レベル          | -    | 地域階層で絞り込み |
| cdArea           | 地域事項 単一コード          | -    | 地域コード指定 |
| cdAreaFrom       | 地域事項 コード From         | -    | 地域コードの範囲（開始） |
| cdAreaTo         | 地域事項 コード To           | -    | 地域コードの範囲（終了） |
| lvCat01 ~ lvCat15| 分類事項01〜15 階層レベル     | -    | 最大15分類対応 |
| cdCat01 ~ cdCat15| 分類事項01〜15 単一コード     | -    | 対応する項目コード指定 |
| cdCatXXFrom/To   | 分類事項XX コード範囲指定    | -    | 範囲指定に使用 |

---

#### 注意点・仕様補足

- `statsDataId` または `dataSetId` のいずれか一方は必須です。両方指定するとエラーになります。
- `min` / `max` という特別なキーワードをコード指定に使うことも可能です。
- 絞り込み条件はすべて AND 条件で適用されます。
- `statsDatasSpec` は JSON 配列であり、複数のリクエストをまとめて送信できます。
- リクエストにはサーバ側でリクエスト番号（1からの連番）が自動で付与され、エラー時の識別に使用されます。

---

#### 制限事項

- 全リクエストの統計データ件数の合計が **100,000件** を超えるとエラーになります。
- 統計データ一括取得の `limit` パラメータは個別リクエストごとに定義可能です。

---

#### エラー例（共通）

- コード数オーバー、フォーマット違反、未認証のアプリケーションIDなどの場合、HTTPステータスとメッセージが返されます。


## 4. APIの出力データ

各APIは、指定された出力形式（XML、JSON、JSONP、CSV）に応じたデータ構造を返します。

### 出力形式の共通構造（XML形式）

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<GET_STATS_LIST
  xsi:noNamespaceSchemaLocation="http://api.e-stat.go.jp/rest/<バージョン>/schema/GetStatsList.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <RESULT>...</RESULT>
  <PARAMETER>...</PARAMETER>
  <DATALIST_INF>...</DATALIST_INF>
</GET_STATS_LIST>
```

- `<RESULT>`：APIの処理結果（ステータスコード、メッセージ、出力日時など）
- `<PARAMETER>`：受信したパラメータ情報
- `<DATALIST_INF>`：統計表情報、メタ情報、統計データなど、API固有の出力内容

---

### JSON形式への変換ルール

| XML構造 | JSON変換例 |
|--------|-------------|
| `<タグ名>値</タグ名>` | `"タグ名": "値"` |
| `<タグ 属性="値">内容</タグ>` | `"タグ": { "@属性": "値", "$": "内容" }` |
| 同名タグの繰り返し | `"タグ": [ {"$": "値1"}, {"$": "値2"} ]` |

---

### JSON出力における特殊文字のエスケープ

| 文字 | エスケープ文字 |
|------|----------------|
| `<`  | `\u003c`       |
| `>`  | `\u003e`       |
| `&`  | `\u0026`       |
| `=`  | `\u003d`       |
| `'`  | `\u0027`       |
| `"`  | `\"`           |
| `\`  | `\\`           |

---

### CSV形式における出力ルール

- 各項目はダブルクォート `"` で囲まれる
- 区切りはカンマ `,`
- 項目に `"` を含む場合は `""` としてエスケープ
- 項目順は固定（タグ名、タグ値の順）

---

## 4.1 全API共通の出力

### `<RESULT>` タグの構成

| タグ名     | 内容 |
|------------|------|
| `<STATUS>` | APIの処理結果コード（`0`：正常、`1`：正常だがデータなし、`100`以上はエラー） |
| `<ERROR_MSG>` | 結果に応じたメッセージ |
| `<DATE>`   | 出力日時（ISO 8601形式） |

#### ステータスコード一覧（STATUS + ERROR_MSG）

| コード | HTTPステータス | メッセージ例 | 内容 |
|--------|----------------|--------------|------|
| 0      | 200            | 正常に終了しました。 | 正常終了 |
| 1      | 200            | 該当データはありませんでした。 | データなし（正常） |
| 2      | 200            | リクエスト番号({0})で該当データはありませんでした。 | 一括取得用 |
| 100    | 403            | 認証に失敗しました。 | appIdの誤り |
| 101    | 400            | {0}を指定して下さい。 | 必須パラメータ未指定 |
| 102    | 400            | {0}の値が正しくありません。 | 無効な値 |
| 103    | 400            | {0}の値が長すぎます。{1}バイト以内で指定して下さい。 | 長さ超過 |
| 104    | 400            | {0}に使用できる文字は{1}です。 | 不正文字 |
| 105    | 400            | {0}の値が多すぎます。100個以内で指定して下さい。 | 単一コード過多 |
| 200〜203 | 500          | 各種内部エラー（DBアクセスエラーなど） | システム障害 |
| 299    | 500            | 予期しないエラーが発生しました。 | その他システムエラー |
| 300    | 400            | {0}=[{1}]のデータは存在しません。 | 存在しないIDなど |
| 301    | 200            | 更新・削除の権限がありません。 | 他アプリIDのデータ変更 |
| 302    | 200            | 絞込条件による抽出件数が0件です。 | データセット登録時 |
| 303    | 500            | データセットIDの自動付与に失敗しました。 | サーバ内部処理エラー |
| 400    | 200            | 返却セルデータ数が多すぎます。 | 一括取得上限超過（100,000件） |
| 401    | 500            | リクエスト番号 {0} でエラー{1}：{2} | 一括取得内の個別エラー詳細 |

## 4.2 統計表情報取得

この出力は `getStatsList` API 呼び出しに対して返される内容です。

---

### 4.2.1 PARAMETER タグ

リクエスト時に指定された各パラメータが `<PARAMETER>` 内に出力されます。

| タグ名               | 内容                           |
|----------------------|--------------------------------|
| `<LANG>`             | 言語（J：日本語、E：英語）       |
| `<DATA_FORMAT>`      | 出力形式（X：XML、J：JSON）     |
| `<SURVEY_YEARS>`     | 調査年月                        |
| `<OPEN_YEARS>`       | 公開年月                        |
| `<STATS_FIELD>`      | 統計分野コード                  |
| `<STATS_CODE>`       | 政府統計コード（作成機関コード）|
| `<SMALL_AREA>`       | 小地域対象フラグ                |
| `<SEARCH_WORD>`      | 検索キーワード                  |
| `<SEARCH_KIND>`      | 検索データ種別                  |
| `<COLLECT_AREA>`     | 集計地域                        |
| `<EXPLANATION_GET_FLG>` | 解説出力有無                |
| `<STATS_NAME_LIST>`  | 調査名一覧出力フラグ（Y指定時） |
| `<START_POSITION>`   | 開始行                          |
| `<LIMIT>`            | 最大取得件数                    |
| `<UPDATED_DATE>`     | 更新日付                        |
| `<CALLBACK>`         | JSONP用コールバック関数名       |

---

### 4.2.2 DATALIST_INF タグ

統計表情報本体が `<DATALIST_INF>` タグ以下に格納されます。該当データが無い場合はこのタグ自体が出力されません。

| タグ名           | 内容                                           |
|------------------|------------------------------------------------|
| `<NUMBER>`       | 出力される統計表件数                          |
| `<RESULT_INF>`   | 結果に関する補足情報（取得範囲・継続キーなど） |
| `<FROM_NUMBER>`  | データの取得開始行                            |
| `<TO_NUMBER>`    | データの取得終了行                            |
| `<NEXT_KEY>`     | 継続取得用の次の取得開始位置                  |
| `<TABLE_INF>`    | 各統計表情報（複数）                          |

---

### TABLE_INF 内部構成（1統計表あたり）

| タグ名                            | 内容                                               |
|-----------------------------------|----------------------------------------------------|
| `@id`                             | 統計表ID                                           |
| `<STAT_NAME code="">`             | 政府統計名、属性に統計コード                     |
| `<GOV_ORG code="">`              | 作成機関名、属性に機関コード                     |
| `<STATISTICS_NAME>`              | 提供統計名＋分類名                                |
| `<TITLE no="">`                  | 表題、属性に表番号                                |
| `<CYCLE>`                        | 提供周期（例：年次、月次）                        |
| `<SURVEY_DATE>`                  | 調査年月                                          |
| `<OPEN_DATE>`                    | 公開日                                            |
| `<SMALL_AREA>`                   | 小地域属性（0：対象外、1：対象）                 |
| `<COLLECT_AREA>`                | 集計地域（全国、都道府県等）                     |
| `<MAIN_CATEGORY code="">`       | 統計大分類名、属性にコード                       |
| `<SUB_CATEGORY code="">`        | 統計小分類名、属性にコード                       |
| `<OVERALL_TOTAL_NUMBER>`        | 絞り込み無しの統計データ件数                     |
| `<UPDATED_DATE>`                | 最終更新日                                        |
| `<STATISTICS_NAME_SPEC>`        | 統計名と分類名の詳細構造                         |
| └ `<TABULATION_CATEGORY>`       | 提供統計名                                        |
| └ `<TABULATION_SUB_CATEGORY1~5>`| 提供分類名（最大5階層）                          |
| `<DESCRIPTION>`                 | 解説文ブロック（省略可能）                        |
| └ `<TABULATION_CATEGORY_EXPLANATION>`       | 提供統計の解説                          |
| └ `<TABULATION_SUB_CATEGORY_EXPLANATION1~5>`| 各提供分類の解説                          |
| `<TITLE_SPEC>`                  | 表題の詳細ブロック                                |
| └ `<TABLE_CATEGORY>`            | 表分類名                                          |
| └ `<TABLE_NAME>`                | 表題                                              |
| └ `<TABLE_EXPLANATION>`         | 表題の解説                                        |
| └ `<TABLE_SUB_CATEGORY1~3>`     | 表題の分類（最大3階層）                          |

※ `<DESCRIPTION>` や `<TABLE_EXPLANATION>` は `explanationGetFlg=N` の場合は出力されません。

---

### 4.2.3 統計調査名一覧モード

`statsNameList=Y` を指定すると、`<DATALIST_INF>` の中身が調査名リストに切り替わります。

| タグ名          | 内容                       |
|-----------------|----------------------------|
| `<LIST_INF>`    | 調査名ごとの情報           |
| `@id`           | 政府統計コード             |
| `<STAT_NAME>`   | 政府統計名（属性：code）   |
| `<GOV_ORG>`     | 作成機関名（属性：code）   |

---

### 4.2.4 XML出力サンプル（通常モード）

```xml
<GET_STATS_LIST>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T17:20:57.716+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <SURVEY_YEARS>201001-201212</SURVEY_YEARS>
    <STATS_FIELD>03</STATS_FIELD>
    <STATS_CODE>00200</STATS_CODE>
    <SEARCH_WORD>就業構造基本調査</SEARCH_WORD>
    <DATA_FORMAT>X</DATA_FORMAT>
    <LIMIT>1000</LIMIT>
  </PARAMETER>
  <DATALIST_INF>
    <NUMBER>543</NUMBER>
    <TABLE_INF id="0003084821">
      <STAT_NAME code="00200532">就業構造基本調査</STAT_NAME>
      <GOV_ORG code="00200">総務省</GOV_ORG>
      <STATISTICS_NAME>平成24年就業構造基本調査 全国編</STATISTICS_NAME>
      <TITLE no="00100">男女，就業状態・仕事の主従，...</TITLE>
      <CYCLE>-</CYCLE>
      <SURVEY_DATE>201210</SURVEY_DATE>
      <OPEN_DATE>2013-07-12</OPEN_DATE>
      <SMALL_AREA>0</SMALL_AREA>
      <COLLECT_AREA>全国</COLLECT_AREA>
      <MAIN_CATEGORY code="03">労働・賃金</MAIN_CATEGORY>
      <SUB_CATEGORY code="01">労働力</SUB_CATEGORY>
      <OVERALL_TOTAL_NUMBER>8208</OVERALL_TOTAL_NUMBER>
      <UPDATED_DATE>2014-02-10</UPDATED_DATE>
    </TABLE_INF>
  </DATALIST_INF>
</GET_STATS_LIST>
```

---


## 4.3 メタ情報取得

この出力は `getMetaInfo` API の呼び出しに対して返される内容です。

---

### 4.3.1 PARAMETER タグ

| タグ名       | 内容                           |
|--------------|--------------------------------|
| `<LANG>`     | 言語（J：日本語、E：英語）       |
| `<DATA_FORMAT>` | 出力形式（X：XML、J：JSON）   |
| `<STATS_DATA_ID>` | 統計データID                |
| `<METAGET_FLG>` | 表定義・表章項目の情報出力フラグ |

---

### 4.3.2 METADATA_INF タグ

- 統計表のメタ情報が格納されるタグ。
- 存在しないID等が指定された場合は出力されない。

#### 主な構造：

| タグ名                  | 内容                                       |
|--------------------------|--------------------------------------------|
| `<METADATA_INF>`         | メタ情報本体タグ                          |
| `<CLASS_INF>`            | 分類情報ブロック                          |
| `<CLASS_OBJ>`            | 分類オブジェクト                          |
| `@id`                    | 分類ID（TIME、AREA、SEXなど）              |
| `<CLASS>`                | 分類項目（複数）                          |
| `@code`                  | 項目コード                                 |
| `@level`                 | 階層レベル                                 |
| `@unit`                  | 単位                                       |
| `<NAME>`                 | 項目名                                     |
| `<CLASS_TITLE>`          | 分類のタイトル                             |
| `<DESCRIPTION>`          | 分類の説明文（省略可能）                  |

---

### 4.3.3 表定義情報（METAGET_FLG=Y の場合）

表の定義や表章項目の詳細情報も出力されます。

#### TABLE_INF タグ構成

| タグ名                     | 内容                               |
|----------------------------|------------------------------------|
| `<TABLE_INF>`              | 表定義情報タグ                     |
| `<STAT_NAME>`              | 政府統計名（code 属性付き）         |
| `<GOV_ORG>`                | 作成機関名（code 属性付き）         |
| `<TITLE>`                  | 表題                               |
| `<UPDATED_DATE>`           | 更新日                             |
| `<EXPLANATION>`            | 表の説明（省略可能）               |
| `<TABLE_SUB_CATEGORY1~3>`  | 表題の分類                         |
| `<TABLE_CATEGORY>`         | 表分類                             |
| `<TABLE_NAME>`             | 表名                               |
| `<TABLE_EXPLANATION>`      | 表の補足説明文（省略可能）         |

---

### 4.3.4 XML出力例

```xml
<GET_META_INFO>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T17:24:12.681+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <STATS_DATA_ID>0003084817</STATS_DATA_ID>
    <METAGET_FLG>Y</METAGET_FLG>
  </PARAMETER>
  <METADATA_INF>
    <CLASS_INF>
      <CLASS_OBJ id="AREA">
        <CLASS code="00000" level="1">
          <NAME>全国</NAME>
        </CLASS>
        <CLASS code="01100" level="2">
          <NAME>北海道</NAME>
        </CLASS>
      </CLASS_OBJ>
    </CLASS_INF>
    <TABLE_INF>
      <STAT_NAME code="00200532">就業構造基本調査</STAT_NAME>
      <GOV_ORG code="00200">総務省</GOV_ORG>
      <TITLE no="00100">男女，就業状態・仕事の主従...</TITLE>
      <UPDATED_DATE>2014-02-10</UPDATED_DATE>
      <TABLE_NAME>労働力調査</TABLE_NAME>
      <TABLE_CATEGORY>労働・賃金</TABLE_CATEGORY>
      <TABLE_SUB_CATEGORY1>労働力</TABLE_SUB_CATEGORY1>
      <TABLE_EXPLANATION>調査概要および提供内容の補足説明</TABLE_EXPLANATION>
    </TABLE_INF>
  </METADATA_INF>
</GET_META_INFO>
```

---

## 4.4 統計データ取得

この出力は `getStatsData` API の呼び出しに対して返される内容です。

---

### 4.4.1 PARAMETER タグ

| タグ名           | 内容                                               |
|------------------|----------------------------------------------------|
| `<LANG>`         | 言語（J：日本語、E：英語）                         |
| `<STATS_DATA_ID>`| 統計データID                                       |
| `<CDCAT01~20>`   | 任意の分類コード（AREA, SEX, TIMEなど）を指定可能   |
| `<START_POSITION>` | 開始位置（ページネーション対応）                 |
| `<LIMIT>`        | 取得件数上限                                        |

---

### 4.4.2 DATA_INF タグ構成

| タグ名           | 内容                                                 |
|------------------|------------------------------------------------------|
| `<DATA_INF>`     | 統計データ情報全体を格納するタグ                     |
| `<VALUE>`        | 実データの値を格納（複数あり）                       |
| `@unit`          | 単位（任意、指定があれば表示）                        |
| `@tab`           | 表章項目コード                                       |
| `@cat01~cat20`   | 分類項目コード（AREA、SEX、TIMEなど）最大20種まで     |
| `@area`          | 地域コード（@catと同等）                             |
| `@time`          | 時間コード（@catと同等）                             |
| `@attr`          | その他属性情報                                       |
| `@annotation`    | 備考・注釈情報の存在有無                             |

---

### 4.4.3 XML出力例

```xml
<GET_STATS_DATA>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T17:35:12.681+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <STATS_DATA_ID>0003084817</STATS_DATA_ID>
  </PARAMETER>
  <STATISTICAL_DATA>
    <CLASS_INF>
      <CLASS_OBJ id="AREA">
        <CLASS code="00000" level="1">
          <NAME>全国</NAME>
        </CLASS>
      </CLASS_OBJ>
    </CLASS_INF>
    <DATA_INF>
      <VALUE tab="001" cat01="0001" area="00000" time="2010000101" unit="人">12000000</VALUE>
      <VALUE tab="001" cat01="0002" area="00000" time="2010000101" unit="人">8000000</VALUE>
    </DATA_INF>
  </STATISTICAL_DATA>
</GET_STATS_DATA>
```

---

### 4.4.4 備考

- `cat01〜cat20` で複数の分類軸を同時に管理
- `annotation` が存在する場合、別タグで詳細を確認可能
- JSONやCSV形式でも同様の項目がキーまたは列として出力される

---

## 4.5 データセット登録

この出力は `saveStatsData` API の呼び出しに対して返される内容です。  
統計データ取得条件を保存し、後から参照可能な「データセット」を生成します。

---

### 4.5.1 PARAMETER タグ

| タグ名           | 内容                                           |
|------------------|------------------------------------------------|
| `<LANG>`         | 言語（J：日本語、E：英語）                     |
| `<STATS_DATA_ID>`| 対象となる統計データID                         |
| `<CDCAT01~20>`   | 分類コード指定（最大20軸）                      |
| `<DATA_SET_COMMENT>` | 任意コメント                                |

---

### 4.5.2 DATASET_INF タグ構成

| タグ名           | 内容                                               |
|------------------|----------------------------------------------------|
| `<DATASET_INF>`  | 登録されたデータセットに関する情報を格納           |
| `<DATASET_ID>`   | 登録完了後に発行されるデータセットID               |
| `<DATE>`         | 登録日時（ISO 8601形式）                          |
| `<COMMENT>`      | ユーザーが登録時に指定したコメント（省略可）       |

---

### 4.5.3 XML出力例

```xml
<SAVE_STATS_DATA>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T17:40:12.681+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <STATS_DATA_ID>0003084817</STATS_DATA_ID>
    <DATA_SET_COMMENT>2020年都道府県別集計</DATA_SET_COMMENT>
  </PARAMETER>
  <DATASET_INF>
    <DATASET_ID>DS0000012345</DATASET_ID>
    <DATE>2015-01-07T17:40:12.681+09:00</DATE>
    <COMMENT>2020年都道府県別集計</COMMENT>
  </DATASET_INF>
</SAVE_STATS_DATA>
```

---

### 備考

- 登録した `DATASET_ID` は後続の `getDataset` や `getStatsDatas` API で利用可能
- データセットは一時保存され、一定期間後に削除されることがあるため注意

---

## 4.6 データセット参照

この出力は `getDataset` API の呼び出しに対して返される内容です。  
事前に `saveStatsData` API で登録されたデータセットを参照します。

---

### 4.6.1 PARAMETER タグ

| タグ名           | 内容                                      |
|------------------|-------------------------------------------|
| `<LANG>`         | 言語（J：日本語、E：英語）                |
| `<DATASET_ID>`   | 対象のデータセットID                      |

---

### 4.6.2 DATASET_INF タグ構成

| タグ名            | 内容                                                   |
|-------------------|--------------------------------------------------------|
| `<DATASET_INF>`   | データセットの全体構成タグ                             |
| `<STATS_DATA_ID>` | 元となる統計データID                                   |
| `<TAB_CODE>`      | 表章項目コード                                         |
| `<CLASS_OBJ>`     | 分類情報（AREA, SEX, TIME など）                       |
| `<DATA_SET_COMMENT>` | ユーザーが登録時に付けたコメント                    |
| `<UPDATED_DATE>`  | データセットの最終更新日時（ISO 8601形式）             |

---

### 4.6.3 XML出力例

```xml
<GET_DATASET>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T17:45:12.681+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <DATASET_ID>DS0000012345</DATASET_ID>
  </PARAMETER>
  <DATASET_INF>
    <STATS_DATA_ID>0003084817</STATS_DATA_ID>
    <TAB_CODE>001</TAB_CODE>
    <CLASS_OBJ id="AREA">
      <CLASS code="00000" level="1">
        <NAME>全国</NAME>
      </CLASS>
    </CLASS_OBJ>
    <DATA_SET_COMMENT>2020年都道府県別集計</DATA_SET_COMMENT>
    <UPDATED_DATE>2015-01-07T17:45:12.681+09:00</UPDATED_DATE>
  </DATASET_INF>
</GET_DATASET>
```

---

### 備考

- 登録時の分類や条件情報がそのまま復元されるため、再利用性が高い
- 結果は `saveStatsData` と同様の構造で取得されるが、出力専用

---

## 4.7 データカタログ情報取得

この出力は `getStatsDataCatalog` API の呼び出しに対して返される内容です。  
統計表ファイルやデータベース（DB）などの情報を一覧形式で取得できます。

---

### 4.7.1 PARAMETER タグ

| タグ名             | 内容                                             |
|--------------------|--------------------------------------------------|
| `<LANG>`           | 言語（J：日本語、E：英語）                       |
| `<SURVEY_YEAR>`    | 調査年                                           |
| `<DATA_TYPE>`      | データタイプ（1: 統計表ファイル, 2: DB, 3: 両方） |
| `<DATASET_ID>`     | 対象のデータセットID（任意）                     |

---

### 4.7.2 CATALOG_LIST タグ構成

| タグ名             | 内容                                               |
|--------------------|----------------------------------------------------|
| `<CATALOG_LIST>`   | カタログ情報の配列構造                             |
| `<STAT_NAME>`      | 統計名                                             |
| `<TITLE>`          | 統計表タイトル                                     |
| `<RELEASE_DATE>`   | 公開日                                             |
| `<FILE_TYPE>`      | ファイル形式（CSV, XLSX など）                     |
| `<DATA_TYPE>`      | データ種別（1: 統計表ファイル, 2: DB）             |
| `<URI>`            | ファイルダウンロードURI                            |

---

### 4.7.3 XML出力例

```xml
<GET_STATS_DATA_CATALOG>
  <RESULT>
    <STATUS>0</STATUS>
    <ERROR_MSG>正常に終了しました。</ERROR_MSG>
    <DATE>2015-01-07T18:00:00.000+09:00</DATE>
  </RESULT>
  <PARAMETER>
    <LANG>J</LANG>
    <SURVEY_YEAR>2020</SURVEY_YEAR>
    <DATA_TYPE>1</DATA_TYPE>
  </PARAMETER>
  <CATALOG_LIST>
    <CATALOG>
      <STAT_NAME>労働力調査</STAT_NAME>
      <TITLE>年齢別労働力人口</TITLE>
      <RELEASE_DATE>2021-03-15</RELEASE_DATE>
      <FILE_TYPE>CSV</FILE_TYPE>
      <DATA_TYPE>1</DATA_TYPE>
      <URI>https://www.e-stat.go.jp/stat-search/file-download?statInfId=0000123456</URI>
    </CATALOG>
  </CATALOG_LIST>
</GET_STATS_DATA_CATALOG>
```

---

### 備考

- 各エントリは `<CATALOG>` タグ内で独立しているため、複数ファイル情報を一括取得可能
- ファイルタイプやURIを用いて直接ダウンロードリンクとして活用可能

---

## 4.8 統計データ一括取得

この出力は `getStatsDatas` API の呼び出しに対して返される内容です。  
複数の統計表IDやデータセットIDを一括して取得できる API です。

---

### 4.8.1 PARAMETER タグ

| タグ名               | 内容                                           |
|----------------------|------------------------------------------------|
| `<LANG>`             | 言語（J：日本語、E：英語）                     |
| `<REQUEST_NUMBER>`   | リクエストごとの識別子                         |
| `<STATS_DATA_ID>`    | 取得対象の統計データID（複数指定可能）         |
| `<DATASET_ID>`       | 登録済データセットID（複数指定可能）           |
| `<OPTIONAL_PARAM>`   | 各リクエストごとに付けられた追加条件パラメータ |

---

### 4.8.2 STATISTICAL_DATA_LIST タグ構成

| タグ名                    | 内容                                                    |
|---------------------------|---------------------------------------------------------|
| `<STATISTICAL_DATA_LIST>` | 各取得結果のリスト                                     |
| `<STATISTICAL_DATA>`      | 個々の統計データ情報ブロック（`getStatsData` 相当）    |
| `<RESULT>`                | 結果ステータス、エラーメッセージ、タイムスタンプなど   |
| `<PARAMETER>`             | 各リクエストに対する入力パラメータ                     |
| `<TABLE_INF>`             | 統計表の基本情報（名称、ID、分類など）                 |
| `<DATA_INF>`              | 実データ部分                                           |

---

### 4.8.3 XML出力例

```xml
<GET_STATS_DATAS>
  <STATISTICAL_DATA_LIST>
    <STATISTICAL_DATA>
      <RESULT>
        <STATUS>0</STATUS>
        <ERROR_MSG>正常に終了しました。</ERROR_MSG>
        <DATE>2021-01-10T15:00:00+09:00</DATE>
      </RESULT>
      <PARAMETER>
        <REQUEST_NUMBER>1</REQUEST_NUMBER>
        <LANG>J</LANG>
        <STATS_DATA_ID>0001234567</STATS_DATA_ID>
      </PARAMETER>
      <TABLE_INF>...</TABLE_INF>
      <DATA_INF>...</DATA_INF>
    </STATISTICAL_DATA>

    <STATISTICAL_DATA>
      <RESULT>
        <STATUS>0</STATUS>
        <ERROR_MSG>正常に終了しました。</ERROR_MSG>
        <DATE>2021-01-10T15:01:00+09:00</DATE>
      </RESULT>
      <PARAMETER>
        <REQUEST_NUMBER>2</REQUEST_NUMBER>
        <LANG>J</LANG>
        <DATASET_ID>DS0000009999</DATASET_ID>
      </PARAMETER>
      <TABLE_INF>...</TABLE_INF>
      <DATA_INF>...</DATA_INF>
    </STATISTICAL_DATA>
  </STATISTICAL_DATA_LIST>
</GET_STATS_DATAS>
```

---

### 備考

- 最大取得件数や同時リクエスト数には制限あり（公式仕様参照）
- リクエスト番号を使って個別の応答を判別可能
- 結果は `getStatsData` と同じ構造で返却されるため既存処理と連携しやすい

---
