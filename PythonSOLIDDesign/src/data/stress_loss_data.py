from dataclasses import dataclass
import pandas as pd

@dataclass
class StressTestData:
    """ストレステストデータを格納するクラス"""
    
    scenario_name: str  # ストレスシナリオ名
    shock_factors: pd.DataFrame  # 株価や金利のショック値
    stress_losses: pd.Series  # 各資産のストレスロス
