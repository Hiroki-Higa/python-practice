# Python Practice

## 概要
Complete Python Bootcampを使ってPythonの基礎学習を開始。
開発環境の構築と、Pythonの基本的な書き方に慣れることが目的。

## Day1：Python基礎（Numbers / Strings）

### 今日やったこと
- Pythonの実行環境を構築（VS Code + Python）
- 数値（int / float）の計算
- 文字列（str）の基本操作
- print文で結果を表示

### 学んだこと・気づき
- Pythonは型を意識しなくても書けるが、型を意識すると読みやすい
- 文字列には便利なメソッド（upperなど）がある

### 次やること
- リストと辞書を使ったデータ管理


# Python Practice

## 概要
Pythonの基本データ構造を学習。
複数のデータをまとめて扱う方法に慣れる。

## Day2：Python基礎（List / Dictionary）

### 今日やったこと
- listの作成、要素の追加・参照
- dictionaryの作成、keyを使ったアクセス
- listとdictionaryを組み合わせたデータ操作

### 学んだこと・気づき
- listは順番付き、dictionaryはkeyで管理する
- 辞書を使うとデータの意味が分かりやすくなる
- Web APIのレスポンスは辞書構造が多そうだと感じた

### 次やること
- 比較演算子とif文で条件分岐を書く

## Day3（アウトプット）
### 今日やったこと
- ユーザー情報をlistとdictで管理するプログラムを作成
- if文とfor文で条件分岐と繰り返し処理を実装

### 学んだこと
- データ構造を先に設計するとコードが書きやすい
- for文の中でdictにアクセスするのに慣れた

### 次やること
- 関数に処理をまとめる

## Day4：条件分岐と繰り返し
### 今日やったこと
- if / elif / else を使った条件分岐
- for / while 文による繰り返し処理
- 条件とループを組み合わせた簡単なロジック作成

### 学んだこと
- 条件分岐で処理の流れを制御できる
- for と while の使い分け
- 処理の回数や終了条件を意識する重要性

### 次やること
- list / dict と条件分岐を組み合わせた演習

## Day5：Python基礎総復習
### 今日やったこと
- 変数・型・list・dict の復習
- 条件分岐とループを組み合わせた演習
- 簡単なロジックを自力で実装

### 学んだこと
- 基礎文法を組み合わせることで実用的な処理が書ける
- エラーが出たときは1行ずつ確認するのが大事
- 小さく動かしながら作ると理解が深まる

### 次やること
- 関数を使った処理の整理（セクション6）


## Day6：関数アウトプット
### 今日やったこと
- 会員区分を判定する関数を作成
- ユーザー情報を関数で処理

### 学んだこと
- 処理を関数に分けると理解しやすい
- returnの使い所が分かってきた

### 次やること
- 複数関数を組み合わせた処理

## Day7：処理フロー設計アウトプット
### 今日やったこと
- ユーザーを追加・検索できるCLIアプリを作成
- whileループと関数を使った処理フロー設計

### 学んだこと
- プログラムの実行状態と入力の違いを理解
- 状態を持つデータを関数で操作する考え方

### 次やること
- クラスを使ったデータ管理

## Day8：クラス（セクション8）
### 今日やったこと
- UserManager クラスを作成
- データ(users)と処理をクラス内にまとめた
- 関数ベースの処理をクラスにリファクタ

### 学んだこと
- __init__ はインスタンス生成時に呼ばれる
- クラスは状態と振る舞いを持つ
- Pythonは上から順に読み込まれる

### 次やること
- クラス設計に慣れる

## Day9：JSONによるデータ保存
### 今日やったこと
- ユーザー情報をjsonファイルに保存
- 起動時にデータを読み込む処理を実装
- クラスとファイル操作を組み合わせた

### 学んだこと
- __init__ は初期化処理に使える
- json形式はWeb APIと相性が良い
- データ永続化でアプリ感が出る

### 次やること
- 例外処理（エラーに強くする）

## Day10：例外処理
### 今日やったこと
- 入力値チェックに try / except を使用
- json読み込みエラー時の対処を実装
- 異常系でも落ちないCLIアプリを作成

### 学んだこと
- 例外処理はプログラムを守る仕組み
- continue / break による制御

## Day11
- ロジックと入出力を分離

## Day12
- 入力チェックを追加
- try/except による例外処理

# Day13: FastAPIでユーザー管理APIを作成

## 学習内容
- FastAPIの基本構造を理解
- Webアプリケーションの起動方法（uvicorn）
- APIエンドポイント（GET / POST）の作成
- Swagger UI（/docs）を使ったAPI操作
- CLIアプリとWebアプリの違いを理解

## 作成したもの
### ユーザー管理API
- ユーザー追加（名前・年齢）
- ユーザー検索
- FastAPI + uvicorn を使用
- Swagger UIからリクエストを送信可能

## 使用技術
- Python
- FastAPI
- uvicorn

## 実行方法
```bash
cd day13
python -m uvicorn main:app --reload

# Day14: FastAPIでAPI設計を理解する

## 学習内容
- FastAPIを使ったAPI設計の基礎
- GET / POST の役割の違い
- Path Parameter の使い方
- Pydantic（BaseModel）によるデータバリデーション
- Swagger UI（/docs）でのAPI操作

## 作成したもの
### ユーザー管理API（設計改善版）
- ユーザー追加（POST /users）
- ユーザー一覧取得（GET /users）
- ユーザー検索（GET /users/{name}）
- 入力値はPydanticで自動バリデーション

## フォルダ構成
```text
day14/
├── main.py
├── user_manager.py
└── models.py

# Day15: FastAPI User Manager（永続化対応）

## 概要

FastAPI を使ったシンプルなユーザー管理 API です。  
ユーザーの「名前」と「年齢」を登録・取得でき、データは JSON ファイルに保存されます。

Day15 では以下を実装しています。

- FastAPI による Web API
- ユーザー情報の JSON ファイル永続化
- パスパラメータを使ったユーザー取得

---

## 使用技術

- Python 3.14
- FastAPI
- Uvicorn
- JSON（簡易データ保存）

---

## フォルダ構成

# FastAPI User Management API（Day15〜Day18）

## 概要
FastAPI を使ってユーザー管理API（CRUD）を段階的に実装する学習プロジェクト。  
Day15〜Day18では、**API設計・バリデーション・レスポンス定義・エラー設計**を通して  
「実務で通用する最小構成」を目標とする。

---

## 使用技術
- Python 3.14
- FastAPI
- Uvicorn
- Pydantic

---

## ディレクトリ構成（例）


---

## Day15：基本CRUDの実装

### 目標
- FastAPI の基本的な CRUD を理解する
- JSON ファイルを使った簡易データ永続化

### 実装内容
- POST /users
- GET /users/{name}
- ユーザー情報を data.json に保存
- UserManager クラスによるロジック分離

### 学び
- FastAPI のルーティング
- uvicorn の起動方法
- モジュール分割の基本

---

## Day16：PUT / DELETE の追加

### 目標
- REST API として CRUD を完成させる

### 実装内容
- PUT /users/{name}
- DELETE /users/{name}
- HTTPException による 404 エラー制御

### 学び
- HTTPメソッドの役割
- status_code の意味
- docs（Swagger）でAPIを確認する流れ

---

## Day17：レスポンス設計とバリデーション

### 目標
- 「docs を見れば仕様が分かるAPI」を作る

### 実装内容
- response_model の導入
- User / UserResponse の分離
- バリデーション（age >= 0）
- 422 Validation Error の理解

### 主なステータスコード
| Code | 意味 |
|----|----|
| 201 | 作成成功 |
| 200 | 取得・更新成功 |
| 204 | 削除成功（レスポンスなし） |
| 404 | ユーザー未存在 |
| 422 | バリデーションエラー |

### 学び
- Pydantic が自動で422を返す仕組み
- Response Schema の役割
- FastAPIが仕様書を生成する理由

---

## Day18：実務視点での整理

### 目標
- 「動く」から「説明できる」APIへ

### 実装内容
- 責務分離の明確化
  - main.py：API層
  - models.py：データ定義
  - user_manager.py：ビジネスロジック
- README に仕様を明文化

### 学び
- 実務では「コード＋説明」がセット
- APIはドキュメントが本体
- 小さくても設計を意識する重要性

---

## エンドポイント一覧

### POST /users
ユーザー作成

**Request Body**
```json
{
  "name": "Taro",
  "age": 30
}


認証・認可設計（Authentication / Authorization）

本プロジェクトでは JWT + FastAPI Dependencies を用いて
認証（Authentication） と 認可（Authorization） を明確に分離して設計している。

1. 設計方針
認証と認可を分ける理由

認証（401 Unauthorized）

「誰か」を判定する

トークンが有効か

ユーザーが存在するか

認可（403 Forbidden）

「何ができるか」を判定する

管理者権限を持つか

これを分離することで、

エラーハンドリングが明確になる

ルータの責務がシンプルになる

将来的な拡張（role制御）が容易になる

2. 認証：get_current_user
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

役割

Authorization ヘッダから JWT を取得

JWT を検証（署名・期限）

token 内の sub（username）からユーザーを取得

認証に失敗した場合は 401 Unauthorized

責務として「やらないこと」

管理者かどうかは判断しない

ビジネスロジックは持たない

👉 「ログイン済みユーザーとは何か」だけを定義

3. 認可：require_admin
def require_admin(
    user: User = Depends(get_current_user),
):

役割

get_current_user を前提とする

user.is_admin をチェック

権限不足の場合は 403 Forbidden

なぜ分けたか

認証が通っていない場合は 401

認証済みだが権限がない場合は 403

HTTPステータスの意味を正しく表現するため。

4. ルータ設計
管理者専用エンドポイント
@router.get("/admin/users")
def list_users(
    admin = Depends(require_admin),
):


ルータ側では「管理者であること」を意識しない

依存関係にすべてを委譲

👉 ルータ = 業務処理だけを書く

5. テストによる設計保証

pytest により以下を保証している：

未ログイン → 401

一般ユーザーで admin API → 403

管理者 → 200

/me はログインユーザーのみアクセス可能

テストは仕様書として機能しており、
認証・認可の振る舞いを壊さない安全網になっている。

6. 今後の拡張想定

is_admin → role: admin / editor / user

require_role("admin") のような汎用認可

Scope / Permission ベース認可

現在の設計はそれらを無理なく追加できる構造になっている。