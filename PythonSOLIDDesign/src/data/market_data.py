from dataclasses import dataclass
import pandas as pd

@dataclass
class MarketData:
    """市場データを格納するクラス"""
    
    prices: pd.DataFrame   # 株価、債券価格など
    interest_rates: pd.DataFrame  # 金利データ
    volatility: pd.DataFrame  # ボラティリティ

