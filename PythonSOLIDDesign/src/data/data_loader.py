import pandas as pd
import json
from pathlib import Path

class DataLoader:
    """データを読み込むクラス"""

    def __init__(self, config_file: str = "file_path.json"):
        """
        コンストラクターで JSON ファイルからディレクトリ情報を読み込む。
        :param config_file: 設定ファイルのファイル名（デフォルト: "file_path.json"）
        """
        current_dir = Path(__file__).resolve().parent.parent.parent  # プロジェクトのルートディレクトリを取得
        print(current_dir)
        config_path = current_dir / "config" / config_file  # "config/" フォルダ内の設定ファイルを指定
        

        if not config_path.exists():
            raise FileNotFoundError(f"設定ファイルが見つかりません: {config_path}")

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                self.base_dirs = json.load(f)  # JSON からディレクトリ情報を取得
        except json.JSONDecodeError as e:
            raise ValueError(f"設定ファイルの JSON 構文エラー: {e}")

    def _get_full_path(self, directory_key: str, file_name: str) -> str:
        """ディレクトリ情報とファイル名を結合し、完全なパスを生成"""
        if directory_key not in self.base_dirs:
            raise ValueError(f"指定されたディレクトリキー '{directory_key}' は設定に存在しません")
        return str(Path(self.base_dirs[directory_key]) / file_name)

    def load_csv(self, directory_key: str, file_name: str) -> pd.DataFrame:
        """CSV ファイルを読み込む"""
        file_path = self._get_full_path(directory_key, file_name)
        return pd.read_csv(file_path)

    def load_excel(self, directory_key: str, file_name: str) -> pd.DataFrame:
        """Excel ファイルを読み込む"""
        file_path = self._get_full_path(directory_key, file_name)
        return pd.read_excel(file_path)

    def load_json(self, directory_key: str, file_name: str) -> pd.DataFrame:
        """JSON ファイルを読み込む"""
        file_path = self._get_full_path(directory_key, file_name)
        return pd.read_json(file_path)

if __name__ == "__main__":
    """データを読み込んで表示するメイン関数"""
    
    print("データを読み込みます...")

    try:
        # DataLoader のインスタンスを作成（設定ファイルを `config/` から読み込む）
        data_loader = DataLoader("file_path.json")

        # 設定ファイルから CSV のパスを取得し、データを読み込む
        csv_path = data_loader.load_csv(directory_key="data", file_name="portfolio.csv")
        print("\n[CSV データ]:")
        print(csv_path.head())

        # 設定ファイルから JSON のパスを取得し、データを読み込む
        json_path = data_loader.load_json(directory_key="data", file_name="portfolio.json")
        print("\n[JSON データ]:")
        print(json_path.head())

    except FileNotFoundError as e:
        print(f"[エラー] ファイルが見つかりません: {e}")
    except ValueError as e:
        print(f"[エラー] 設定ファイルのフォーマットが正しくありません: {e}")
    except Exception as e:
        print(f"[エラー] データの読み込み中に予期しないエラーが発生しました: {e}")