# Python Directory Best Practices

このリポジトリでは、Python プロジェクトのディレクトリ構成に関するベストプラクティスをまとめた。


---

## **📂 FlatArchitecture/**

### **特徴**
- `src/` の直下にモジュールを配置するシンプルな構成。
- 小規模プロジェクトの開発に適している。

### **実行**
- スクリプト

```python
python src/~.py
```

- テスト
```python
pytest tests/~.py
```

- 🚧 工事中：ノートブック
    - setup.pyでやる
```python

```

### **適用例**
- **ユーティリティツール**
- **スクリプトベースのアプリ**
- **小規模な Python パッケージ**

### **ディレクトリ構成**
```python
FlatArchitecture/ 
│── src/ 
│ ├── init.py 
│ ├── module_a.py 
│ └── module_b.py 
│── tests/ 
│ ├── test_module_a.py 
│ └── test_module_b.py 
│── notebooks/ 
│── config/ 
│── data/ 
│── README.md 
│── pytest.ini 
└── setup.py
```

---

## 🚧 工事中： 📂 LayeredArchitecture

### **特徴**
- `src/` 以下に `query/`, `preprocess/`, `train/` などのディレクトリを分ける構成。
- 中～大規模プロジェクトの開発に適している。

### **適用例**
- **ユーティリティツール**
- **スクリプトベースのアプリ**
- **長期運用を前提としたスケーラブルなシステム**

### **ディレクトリ構成**


```python
LayeredArchitecture/ 
│── src/
│ ├── query/ # データ取得（データベース・API からのデータ取得） 
│ │ ├── init.py 
│ │ ├── fetch_data.py 
│ │ └── database.py 
│ ├── preprocess/ # データの前処理（クリーニング・特徴量エンジニアリング） 
│ │ ├── init.py 
│ │ ├── clean_data.py 
│ │ └── feature_engineering.py 
│ ├── train/ # モデル学習（機械学習モデルのトレーニング） 
│ │ ├── init.py 
│ │ ├── model.py 
│ │ └── train_model.py 
│ └── utils/ # 共通関数（ロギング・設定管理） 
│   ├── init.py 
│   ├── logger.py 
│   └── config.py 
│── notebooks/ # Jupyter Notebook での試験・分析 
│── tests/ # 各モジュールごとのテスト 
│ ├── init.py 
│ ├── query/ 
│ │ └── test_fetch_data.py 
│ ├── preprocess/ 
│ │ └── test_clean_data.py 
│ └── train/ 
│   └── test_train_model.py 
│── config/ # 設定ファイル（YAML・JSON） 
│ └── settings.yaml 
│── data/ # データ関連（取得データ・処理後データ・モデル） 
│ ├── raw/ 
│ ├── processed/ 
│ └── models/ 
│── README.md 
│── pytest.ini 
└── setup.py
```


---

## **📌 どの構成を選ぶべきか？**
| **プロジェクトの種類** | **推奨レイアウト** | **理由** |
|-----------------|--------------------|------------------|
| **小規模スクリプト・ツール開発** | `FlatArchitecture/` | シンプルな構成で始めやすい。ファイル数が多いと管理しにくい |
| **中～大規模スクリプト・ツール開発** | `LayeredArchitecture/` | ディレクトリに分けることで中～大規模開発や長期運用に適している |

