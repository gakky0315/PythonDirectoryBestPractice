# Python Directory Best Practices

このリポジトリでは、Python プロジェクトのディレクトリ構成に関するベストプラクティスをまとめています。  
各フォルダは異なるプロジェクト構成の例を示しており、プロジェクトの種類やスケールに応じた適切なディレクトリ設計を学ぶことができます。

---

## **📂 FlatModuleProject/**（フラットモジュールレイアウト）

### **特徴**
- `src/` の直下にモジュールを配置するシンプルな構成。
- 小規模プロジェクトやスクリプトベースの開発に適している。
- テスト (`tests/`) や設定ファイル (`config/`) は分離。

### **適用例**
- **ユーティリティツール**
- **スクリプトベースのアプリ**
- **小規模な Python パッケージ**

### **ディレクトリ構成**
```python
FlatModuleProject/ 
│── src/ 
│ ├── init.py 
│ ├── module_a.py 
│ ├── module_b.py 
│── tests/ 
│── config/ 
│── data/ 
│── README.md 
│── requirements.txt 
│── pytest.ini 
│── setup.py
```


---

## **📂 LayeredMLProject/**（レイヤードアーキテクチャ）

### **特徴**
- `src/` 以下に `query/`, `preprocess/`, `train/` などのディレクトリを分ける構成。
- 機械学習やデータ処理パイプライン向けの設計。
- 各フォルダが「データ取得」「前処理」「学習」などの異なる役割を持つ。

### **適用例**
- **機械学習・データ分析プロジェクト**
- **データパイプライン**
- **長期運用を前提としたスケーラブルなシステム**

### **ディレクトリ構成**


```python
LayeredMLProject/ │── src/
│ ├── query/ # データ取得（データベース・API からのデータ取得） 
│ │ ├── init.py 
│ │ ├── fetch_data.py 
│ │ ├── database.py 
│ ├── preprocess/ # データの前処理（クリーニング・特徴量エンジニアリング） 
│ │ ├── init.py 
│ │ ├── clean_data.py 
│ │ ├── feature_engineering.py 
│ ├── train/ # モデル学習（機械学習モデルのトレーニング） 
│ │ ├── init.py 
│ │ ├── model.py 
│ │ ├── train_model.py 
│ ├── utils/ # 共通関数（ロギング・設定管理） 
│ │ ├── init.py 
│ │ ├── logger.py 
│ │ ├── config.py 
│── tests/ # 各モジュールごとのテスト 
│ ├── init.py 
│ ├── query/ 
│ │ ├── test_fetch_data.py 
│ ├── preprocess/ 
│ │ ├── test_clean_data.py 
│ ├── train/ 
│ │ ├── test_train_model.py 
│── config/ 
# 設定ファイル（YAML・JSON） 
│ ├── settings.yaml 
│── data/ 
# データ関連（取得データ・処理後データ・モデル） 
│ ├── raw/ 
│ ├── processed/ 
│ ├── models/ 
│── notebooks/ 
# Jupyter Notebook での試験・分析 
│── README.md 
│── requirements.txt 
│── pytest.ini 
│── setup.py
```


---

## **📌 どの構成を選ぶべきか？**
| **プロジェクトの種類** | **推奨レイアウト** | **理由** |
|-----------------|--------------------|------------------|
| **小規模スクリプト・ツール開発** | `FlatModuleProject/` | シンプルな構成で管理しやすい |
| **機械学習・データ分析** | `LayeredMLProject/` | データの流れが明確になり、拡張しやすい |
| **中規模アプリ・パッケージ** | `FlatModuleProject/` | `src/` に直接モジュールを配置することで、パッケージ管理しやすい |
| **データパイプライン・大規模ML** | `LayeredMLProject/` | モジュールの役割を明確に分け、スケーラブルな設計が可能 |

---

## **📌 まとめ**
このリポジトリでは、**Python プロジェクトのベストプラクティスに基づいたディレクトリ構成の例を提供** しています。  
プロジェクトの規模や用途に応じて、適切な構成を選んでください！ 🚀

```sh
git clone https://github.com/your-repo/PythonDirectoryBestPractice.git
