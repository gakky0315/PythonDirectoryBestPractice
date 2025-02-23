import pandas as pd
from src.data.portfolio_data import PortfolioData

class AllocationCalculator:
    """ポートフォリオのアロケーション計算を行うクラス"""
    
    def __init__(self, portfolio_data: PortfolioData):
        self.portfolio_data = portfolio_data

    def calculate_allocation(self) -> pd.Series:
        """アロケーション比率を計算"""
        total_value = self.portfolio_data.allocations.sum()
        return self.portfolio_data.allocations / total_value
