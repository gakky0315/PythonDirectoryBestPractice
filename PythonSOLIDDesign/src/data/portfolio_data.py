from dataclasses import dataclass
import pandas as pd

@dataclass
class PortfolioData:
    """ポートフォリオデータを格納するクラス"""
    
    allocations: pd.DataFrame  # 銘柄ごとのアロケーション
    returns: pd.DataFrame  # リターンデータ
    weights: pd.Series  # ポートフォリオのウェイト

    
if __name__ == "__main__":
    from data_loader import *
    """データを読み込んで表示するメイン関数"""

    print("データを読み込みます...")

    try:
        # DataLoader のインスタンスを作成（設定ファイルを `config/` から読み込む）
        data_loader = DataLoader("file_path.json")

        # 設定ファイルから CSV のパスを取得し、データを読み込む
        csv_data = data_loader.load_csv(directory_key="data", file_name="portfolio.csv")
        print("\n[CSV データ]:")
        print(csv_data.head())
        
        # ポートフォリオデータクラスに格納
        portfolio_data  = PortfolioData(
            allocations = csv_data.drop(columns=["return"]),
            returns     = csv_data["return"],
            weights     = csv_data.sum(axis=1) / csv_data.sum().sum()  # 例: ウェイトの正規化
        )

        print("\n[Portfolio Data - Allocations]:")
        print(portfolio_data.allocations.head())

        print("\n[Portfolio Data - Target]:")
        print(portfolio_data.returns.head())

        print("\n[Portfolio Data - Weights]:")
        print(portfolio_data.weights.head())

    except FileNotFoundError as e:
        print(f"[エラー] ファイルが見つかりません: {e}")
    except ValueError as e:
        print(f"[エラー] 設定ファイルのフォーマットが正しくありません: {e}")
    except Exception as e:
        print(f"[エラー] データの読み込み中に予期しないエラーが発生しました: {e}")
