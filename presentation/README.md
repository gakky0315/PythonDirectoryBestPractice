```python
# 11 Pythonのパッケージの作成と配布

## 11.2 ライブラリのパッケージ作成と配布

### 11.2の全体像

```text
11.2 ライブラリのパッケージ作成と配布
   ├─ 11.2.1 パッケージの基本構成
   │      └─ ディレクトリ構成 / setup.py / setup.cfg / MANIFEST.in
   │
   ├─ 11.2.2 配布物の種類
   │      ├─ ソース配布物（sdist）
   │      └─ バイナリ配布物（bdist / wheel）
   │
   ├─ 11.2.3 PyPI への登録と公開方法（twine）
   │
   ├─ 11.2.4 バージョンと依存関係の管理
   │      ├─ セマンティックバージョニング（SemVer）
   │      └─ カレンダーバージョニング（CalVer）
   │
   ├─ 11.2.5 自分のパッケージをインストールする方法
   │      ├─ setup.py install
   │      ├─ pip install
   │      └─ 編集可能モード（-e）
   │
   └─ 11.2.6 名前空間パッケージの使い方
          ├─ ダメな構成
          └─ 良い構成（PEP 420）




### 11.2.1 Pythonパッケージの構成

Pythonのコードを配布する際にの最小単位はモジュールである。
モジュールは.py拡張子のファイル1つで、こういったモジュールの集合をパッケージと呼ぶ。

この本の筆者がよく使うディレクトリ構成は以下。
```python
.
├── packagename/         ← 実装コード（パッケージの本体）
│   ├── __init__.py
│
├── tests/               ← テストコード
│   ├── __init__.py
│   └── conftest.py
│
├── bin/                 ← スクリプト（CLI用など）
├── data/                ← 学習済みモデル・画像・辞書などのデータ
├── docs/                ← ドキュメント（SphinxやMkDocs用）
│------【以降は入れることが推奨】------
├── README.md            ← パッケージの概要・使い方
├── LICENSE              ← ライセンス（MIT, GPLなど）
├── setup.py             ← パッケージのメタデータ定義と配布用スクリプト
├── setup.cfg            ← setup.pyの補助設定ファイル。setup.pyスクリプトのパラメータを設定しておくことができる。
├── pyproject.toml       ← PEP 621準拠の新しいメタデータ定義ファイル
├── MANIFEST.in          ← 配布に含めるファイルの指定
└── CHANGELOG.md         ← 変更履歴

```

一部のファイルに記法について解説。

#### setup.py
```python
from setuptools import setup

setup(
 name = "mypackage",
)


上記が最小構成であり、PyPIのようなパッケージレジストリに登録することができる。  
しかし、パッケージ配布物を作るという観点では不十分。
以下のようなメタデータを入れることが推奨される。  
- **version**: パッケージのバージョン
- **description**: 短い説明
- **long_description**: 詳しい説明（reStructuredText / Markdown 可）
- **long_description_content_type**: 例 `"text/markdown"`
- **keywords**: 検索用キーワード（カンマ区切りやリスト）
- **author / author_email**: 作者情報
- **url / project_urls**: リポジトリやドキュメント等へのURL
- **license**: ライセンス名
- **packages / py_modules**: 含めるパッケージ／単一モジュール
- **install_requires**: ランタイム依存関係
- **extras_require**: 追加機能のオプション依存
- **python_requires**: 対応Pythonバージョン（例 `">=3.9"`）
- **classifiers**: PyPI 検索用カテゴリ。開発段階、対応OS・Python版、ライセンス等を示す
  - 例：`"Programming Language :: Python :: 3"`, `"License :: OSI Approved :: MIT License"`


#### setup.cfg
setup.pyスクリプトのコマンドのデフォルトオプションを含むファイル。  
パッケージのビルドや配布の手順が複雑で、さまざまなオプション引数をsetup.pyスクリプトに渡さなければらならない時に便利。  
また、プロジェクトに依存した配布フローを明示でき、パッケージがどのようにビルドされ配布されるかが、ユーザーやほかのチームメンバー対してより明瞭

```python
[global]
quiet = 1
[sdist]
formats = zip, tar
[bdist_wheel]
universal = 1


#### MANIFEST.ini
sdistコマンドを使ってソース配布物を作成する時、setup()関数の引数でファイルを指定しない場合、自動的にディレクトリ下のファイル全てがアーカイブに含まれる。また、指定する場合もsetups()関数の引数で指定するのは、手間がかかる。  
その際に、このファイルを使用することで、含めたいファイル名、含めたくないファイル名のパターンを指定できる。
```python
include HISTORY.txt
include README.md
include LICENSE
recursive-include *.md



---

### 11.2.2 パッケージ配布物の種類
Pythonのパッケージ配布物は大きく分けて2つである。
- ソース配布物
- ビルド済み（バイナリ）配布物
    - bdist
    - wheel

#### ソース配布物
- 概要  
最もシンプルでプラットフォーム依存が一番少ない方式である。そのため、高いポータビリティを持っている。
しかし、パッケージにC言語などで書かれた拡張機能が含まれている場合は少し複雑であり、ソース配布物の方式では適していない。

- 作成方法  
ソース配布物はsetup.pyのsdistコマンドで作成するため、sdist配布物とも呼ばれている。
以下にsdistを使用した配布物作成の手順を示す。

1. setup.pyにバージョンを定義する
```python
from setuptools import setup

setup(name = "acme.sql", version = "0.1.1")

2. sdistコマンド実行
```python
$ python setup.py sdist


すると以下のような配布物が出力される
「ディレクトリ構成 or 写真貼る」

#### ビルド済み配布物

- 概要  
ソース配布物とは異なり、コンパイル済みのコードや環境依存のバイナリ形式を含むため、インストールが高速になる。bdistとwheelによって実現可能。

##### bdsit
- 作成方法  
以下のコマンドでバイナリ配布物を作成可能

```python
$ python setup.py bdist


上記のコマンドを実行すると次のような4つのサブコマンドが必要に応じて呼び出される

| サブコマンド       | 役割の概要 |
|---|---|
| `build_py`      | Python モジュールをバイトコード化し `build/` に配置 |
| `build_clib`    | C ライブラリをビルド |
| `build_ext`     | C 拡張モジュールをビルドし `build/` に出力 |
| `build_scripts` | CLI 等のスクリプトをビルド（シバンや実行権限の調整など） |

ビルドを行った環境と**同じシステム向けの成果物**が生成される。  
つまり、**Windowsで作成したらWindows向け**、**macOSで作成したらmacOS向け**の成果物が生成される。
    
- **C拡張をビルドする場合の準備例**
  - Linux：`python3-dev` / `python3-all-dev` など
  - macOS：Xcode Command Line Tools
  - Windows：Build Tools for Visual Studio 2022 など


##### wheel
bdist_wheelコマンドを使用することでプラットフォーム依存の配布物が作成できる
メリット
- ピュアPythonおよびネイティブC拡張パッケージの高速なインストール
- インストールに当たって、なんらかの特徴的なコードの実行が不要（setup.pyが不要）
- WindowsやmacOS、LinuxへのC拡張のインストールでコンパイラが不要
etc


---


### 11.2.3 パッケージの登録と公開
PyPIにユーザー登録をすれば、だれでも新しいパッケージを自由にアップロードすることができる。  
2017年まではsetup.py uploadコマンドを使っていたが、サービス終了したので、現在はTwineを使うことが推奨される。  
Twineは、より安全にパッケージをPyPIのレポジトリにアップロードするというただ1つの目的を達成するためのユーティリティ。Twineを使用する前に、配布物をビルドするためにsetup.pyスクリプトを実行しておく必要がある。

```python
$ python setup.py adist bdist_wheel
$ twine upload dist/*


TwineはPyPIの認証情報を.pypircから取得する。これはPythonパッケージのレポジトリ情報を格納する設定ファイル

- **認証情報（例：`~/.pypirc`）**
```ini
[pypi]
repository = <レポジトリURL>
username = <ユーザー名>
password = <パスワード>


---
### 11.2.4 パッケージのバージョンと依存の管理
リリースするごとにバージョン指定子タグをパッケージにつけて公開する。

バージョン番号自体のつけ方は大きく分けると2つ
- セマンティックバージョニング
- カレンダーバージョニング

#### セマンティックバージョニング
SemVer仕様は、バージョン識別子を3つの部分で構成された数字としている

形式：`MAJOR.MINOR.PATCH`
- **MAJOR**：後方互換 **破壊** を伴う変更（例：1.x → 2.0.0）
- **MINOR**：後方互換を保った機能追加（例：1.2 → 1.3.0）
- **PATCH**：バグ修正等の微修正（例：1.2.1 → 1.2.2）
- 例：`1.4.2`, `2.0.0`

#### カレンダーバージョニング
リリース日付や年・月をバージョンに反映する。
  - 例：`YYYY.MM.DD`（`2025.08.20`）、`YYYY.MM`（`2025.08`）、`YY.MINOR`（`25.3`）など

**使い分けの目安**
- API 互換性と変更の意味を厳密に伝えたい → **SemVer**
- 頻繁にリリース、日付基準での追跡が重要 → **CalVer**


---
### 11.2.5 自分のパッケージをインストールする
インストールの仕方は2つある
- setup.py
- pip

#### setup.py
以下のコマンドでインストールする

```python
$ python setup.py install

- 初めてのビルドであれば、パッケージをビルドしてからその成果物をPythonのパッケージファイルを置くディレクトリ（site-packages/）に配置してくれる　　
- ソース配布物からインストールしたい場合は、一時フォルダに展開してからこのコマンドを使ってインストール可能

#### pip
以下のどちらか。パッケージ配布物の場合は後者
```python 
$ pip install <プロジェクトパス>
$ pip install <アーカイブパス>



#### 編集モード
また、**開発中場合** はコードの変更がある度、毎回アップロード&インストールの手順を踏むのは面倒であるため、常にディレクトリにあるものを直接参照してほしい。  
そのためのインストール方法として、「編集可能モード」と呼ばれるものがある。  
installコマンドに-eまたは、--deitableパラメータを追加すると有効になる  
```python
$ python install -e <プロジェクトパス>


---

### 11.2.6 名前空間パッケージ
#### そもそも名前空間パッケージとは  
Python におけるパッケージの一種で、同じトップレベルのパッケージ名を複数の独立したプロジェクトで共有できる仕組み。  
通常のパッケージは「1つのディレクトリ = 1つのパッケージ」という形でしか作れませんが、  
名前空間パッケージを使うと 複数のディレクトリが 1つのパッケージ名を構成する ことが可能になります。  

#### ダメな構成（通常の場合）
以下の構成だと新しくtemplatingサブパッケージを追加しようとした際に、acme.sqlとacme.templatingパッケージを独立して開発するのが難しい。
```python
acme/
├── acme/
│   ├── __init__.py
│   └── sql/
│       └── __init__.py
├── setup.py

↓
```python
acme/
├── acme/
│   ├── __init__.py
│   ├── sql/
│   │   └── __init__.py
│   └── templating/
│       └── __init__.py
├── setup.py

1つのプロジェクト内に両方入っているため、**acme.sql と acme.templating を独立開発しにくい**。


#### 名前空間パッケージを使った良い構成
目的
- `acme.sql` と `acme.templating` を **独立して開発・配布** したい  
- トップレベル `acme` を **共通の名前空間** にしたい

解決策：
- 各サブパッケージを **個別のプロジェクト** に分離する

```python
acme.sql プロジェクト：
acme.sql/
├── acme/
│   └── sql/
│       └── __init__.py
└── setup.py

acme.templating プロジェクト：
acme.templating/
├── acme/
│   └── templating/
│       └── __init__.py
└── setup.py

この構成により：
- 各プロジェクトは完全に独立！
- `pip install acme.sql` だけで `acme.sql` のみ導入可能
- 必要に応じて `pip install acme.templating` を追加導入できる

#### 補足
上記の名前空間パッケージを使用すると、それぞれ別々のリポジトリ/配布物として存在する。
しかし、インストールするとユーザー側からは次のように見える：
```python
import acme.sql
import acme.templating

両方とも acme 名前空間の下に自然に並ぶ。

## 11.3 Webアプリケーションのためのパッケージ作成


### 11.3 の全体像（関係図）

```text
11.3 Webアプリケーションのためのパッケージ作成
   ├─ 11.3.1 Twelve-Factor App 宣言
   │      ├─ 保守性・スケーラビリティ・移植性
   │      └─ 12の原則（コードベース / 設定 / プロセス …）
   │
   ├─ 11.3.2 Docker の有効性
   │      ├─ 環境の一貫性
   │      ├─ 再現性
   │      ├─ 移植性
   │      └─ Kubernetes（大規模運用・オーケストレーション）
   │
   ├─ 11.3.3 環境変数の扱い
   │      ├─ なぜコードに埋め込まないのか（セキュリティ・柔軟性）
   │      ├─ os.environ の利用
   │      └─ environ-config による型変換・バリデーション
   │
   └─ 11.3.4 フレームワークにおける環境変数の役割
          ├─ アプリケーション構造定義（共通設定）
          └─ 実行時設定（環境ごとに切替）


---


SaaSの登場によって、利用者のコンピュータにインストールするソフトウェア配布形式は少なくなってきている。  
以下の表は、従来型アプリとWebアプリの違いをまとめたもの。  

| 項目       | 従来型アプリ                               | Webアプリ（SaaS）                             |
|------------|------------------------------------------|----------------------------------------------|
| 配布方法   | CDやインストーラーを利用者に渡す          | クラウド上にホスティングし、ブラウザでアクセス |
| 更新方法   | 利用者が自力でアップデート                | 開発者側で即時更新（SaaS）                |
| 例         | Excel, Word                              | Google Docs, Gmail      |       

---

### 11.3.1 Twelve-Factor App宣言
webアプリは従来のものと比べ、早急な問題の修正や多くの利用者を獲得しやすくなっている。
そのため、持続的な成長を可能にするソフトフェアを構築することは非常に重要であり、それを実現するために必要な思想が大事である。

Twelve-Factor App宣言とは、「保守性・スケーラビリティ・移植性」に優れたWebアプリを作るための12の原則

| 原則                 | 内容（要約） |
|----------------------|-------------|
| コードベース         | 1つのコードベースをバージョン管理し、複数のデプロイへ展開 |
| 依存関係             | 外部ライブラリはすべて明示的に管理 |
| 設定                 | 環境ごとの設定は環境変数で注入 |
| バックエンドサービス | DBやキャッシュをアタッチリソースとして扱う |
| ビルド/リリース/実行 | 各フェーズを明確に分離 |
| プロセス             | アプリはステートレスなプロセスとして実行 |
| ポートバインディング | ポートを介してサービスを公開 |
| 並行性               | 複数プロセスでスケールアウト |
| 廃棄容易性           | シャットダウン時に即終了できる設計（graceful shutdown） |
| 開発・本番一致       | 開発/ステージング/本番で同じ環境で動かす |
| ログ                 | ログはファイルに書かず、ストリームに出力 |
| 管理プロセス         | DBマイグレーション等を一時プロセスで実行 |
詳細：https://12factor.net/ja

---

### 11.3.2 Dockerの有効性
**Docker** とは、アプリケーションと実行環境（OS・ライブラリ・設定）をまとめて1つのイメージにできる技術。 
-> どこでも同じ環境を再現できる。（詳細は第2章）

#### Dockerの利点（Twelve-Factor Appとの対応）
| 概念             | 内容 | Twelve-Factorとの関係 |
|------------------|------|------------------------|
| 環境の一貫性     | 同じイメージを利用して差異を排除 | 「開発・本番一致」 |
| 再現性           | 誰でも同じ環境を構築可能 | 「ビルド・リリース・実行」分離 |
| 移植性           | OSを問わず動作可能 | 「ポータビリティ」 |

#### Kubernetes
大規模運用では Docker だけでは不十分（例：分散配置・スケーリング・障害耐性）。 
そこで登場するのがKubernetes
Kubernetesは、Dockerコンテナの数・配置・実行・回復・通信を一元管理するためのオーケストレーションツールである。
つまり、コンテナを大量に自動運用するための管理ツールである。

---

### 11.3.3 環境変数の扱い
#### 概要
アプリケーションごとに異なる設定が必要になるため、環境変数が必要。   
以下のような情報を外部から注入するために使われる  
- DB接続URL、ホスト名、ポート番号など
- 認証情報（APIキー、パスワードなど）
- 環境による設定の切り替え（本番・開発）

#### コードに組み込んではいけない理由
- **セキュリティ**: パスワードやキーが漏洩する危険がある  
- **柔軟性**: 環境による設定切替が容易になる  
- **再現性・移植性**: 他人の環境でも同じ手順で動かせる
    
#### 環境変数の基本的な使い方
- exportコマンドから代入
- 環境変数のファイルを使用（後述）
- API経由で設定

#### pythonでの環境変数の読み込み
- os.environ
- environ-config

##### os.environ
どこからでも参照できるが、一般的な慣習として環境変数にアクセスするモジュールは1つにする。


```python
from datetime import timedelta
import os

DATABASE_URI = os.environ["DATABASE_URI"]
ENCRYPTION_KEY = os.environ["ENCRYPTION_KEY"]

BIND_HOST = os.environ.get("BIND_HOST", "localhost")
BIND_PORT = int(os.environ.get("BIND_PORT", "80"))

SCHEDULE_INTERVAL = timedelta(
    seconds=int(os.environ.get("SCHEDULE_INTERVAL_SECONDS", 50))
)


##### environ-config
環境変数の数が多くなってきたら、設定オブジェクトにまとめ、値の型変換や設定の構造を自動化するのが良い。  
そういったユーティリティライブラリの1つである、environ-configは環境変数名の接頭辞を自動的に解釈して環境変数をグルーピングしてくれる。  
また、値のバリテーションと変換も簡単にしていることができる  

```python
from datetime import timedelta
import environ

environ.config(prefix="")

class Config:
    class Bind:
        host = environ.var(default="localhost")
        port = environ.var(default="80", converter=int)

    bind = environ.group(Bind)

    database_uri = environ.var()
    encryption_key = environ.var()

    schedule_interval = environ.var(
        name="SCHEDULE_INTERVAL_SECONDS",
        converter=lambda value: timedelta(seconds=int(value)),
        default=50
    )


---

### 11.3.4 アプリケーションフレームワークにおける環境変数の役割
Djangoフレームワークでは、設定の役割はsettings.pyモジュールが担っている。これには、アプリケーションで参照する全ての設定値が集まれている。
以下の二つの重要な定義が存在
- アプリケーションの構造定義
    - アプリケーションの「枠組み」を定義する。 
    - 実行時に必須の設定。環境によらず共通
- 実行時設定の定義
    - 主に「どこで、どう動くか」を決める情報。  
    - 環境に応じて切り替わるべき設定

#### 課題
設計はシンプルであるが、欠点もいくつか存在
- **設定の引き回し**: 同じ設定を複数箇所にコピーしやすく、管理ミスの原因に  
- **環境追加が大変**: 環境が増えるたびに新しい設定ファイルが必要  
- **設定変更 = リリース**: 設定を変えるだけで再パッケージが必要

#### Twelve-Factor App に基づいたベストプラクティス
- 推奨される原則：  
| 原則 | 内容 |
|------|------|
| 1つの設定モジュールを使う | 環境ごとの切替は環境変数で行う |  
| 環境依存値を環境変数に持たせる | 設定ファイルは共通化、差分は環境変数で注入 |  
| デフォルトは開発環境向け | 本番では環境変数で上書きする前提で記述 |  
| 機密情報は環境変数に含める | APIキーやパスワードは `.env` やセキュアな設定から注入 |  

---

## 11.4 スタンドアローン実行形式の作成

スタンドアローン実行形式とは、Pythonがインストールされていない環境でもアプリが実行可能。  
これは、pythonスクリプトとライブラリを全て1つの実行ファイル（例：.exe）にまとめる方法である。

---

### 11.4.1 スタンドアローン実行形式が便利なシーン
- ユーザーが Python を知らなくても実行できる。
- 複雑な依存環境の構築が 不要。
- Windows や macOS のユーザーにGUIアプリ感覚で渡せる。
- 商用配布・初心者向けツール配布にも有効。

### 11.4.2 人気のあるツール
以下が挙げられる。
| ツール名      | 主な特徴 |
|---------------|-------------------------------------------|
| **PyInstaller** | 最もよく使われる。Windows / Linux / macOS に対応 |
| **cx_Freeze**   | 学術・業務向けアプリで利用例が多い |
| **py2exe**      | Windows専用。古くからある定番 |
| **py2app**      | macOS専用。GUIアプリ開発に便利 |

どのツールを使用するかは、プロジェクトの開始直後に行うことで、パッケージのビルドを行うためにコードの深いとこまで修正する必要がない。

#### PyInstaller
スタンドアローンの実行形式にまとめるツールの中では最も先進的なプログラム。  
マルチプラットフォーム音互換性が最も広く、一番推奨されている。  
対応プラットフォームは、Windows・Linux・macOS・FreeBSD Solaris OpenBSD  
※クロスプラットフォームのビルドには対応していないので、注意

##### 使い方
myscript.pyというスクリプトに書かれたアプリをビルドするとした時は以下のコマンドで実行可能

```bash
D:\dev\app> pyinstaller myscript.py


ディレクトリ
```python
C:.
│   myscript.py
│   myscript.spec
│
├───build
│   └───myscript
│       │   Analysis-00.toc
│       │   base_library.zip
│       │   COLLECT-00.toc
│       │   EXE-00.toc
│       │   myscript.exe
│       │   myscript.exe.manifest
│       │   myscript.pkg
│       │   PKG-00.toc
│       │   PYZ-00.pyz
│       │   PYZ-00.toc
│       │   warn-myscript.txt
│       │   xref-myscript.html
│       └───localpycs
│           (...)
│
└───dist
    └───myscript
        │   api-ms-win-core-com-l1-1-0.dll
        │   (...)
        │   myscript.exe
        │   python310.dll
        │   (...)


.dllファイルやコンパイル済みの拡張ライブラリなどの追加ファイルもアプリ実行時に必要であるため、このdist/語と渡す必要がある。

もっとコンパクトな生成物を作成する場合、以下のコマンドを実行する
```bash
D:\dev\app> pyinstaller --onefile myscript.py


ディレクトリ
```python
C:.
│   myscript.py
│   myscript.spec
│
├───build
│   └───myscript
│       │   Analysis-00.toc
│       │   base_library.zip
│       │   COLLECT-00.toc
│       │   EXE-00.toc
│       │   myscript.exe
│       │   myscript.exe.manifest
│       │   myscript.pkg
│       │   PKG-00.toc
│       │   PYZ-00.pyz
│       │   PYZ-00.toc
│       │   warn-myscript.txt
│       │   xref-myscript.html
│       └───localpycs
│           (...)
│
└───dist
    └───myscript.exe




名前空間パッケージ
```bash
# acme.sql プロジェクト作成
mkdir acme.sql\acme\sql -Force
ni acme.sql\acme\sql\__init__.py -Force
ni acme.sql\setup.py -Force

# acme.templating プロジェクト作成
mkdir acme.templating\acme\templating -Force
ni acme.templating\acme\templating\__init__.py -Force
ni acme.templating\setup.py -Force
```