import numpy as np
import pandas as pd
from src.data.portfolio_data import PortfolioData

class RiskMetrics:
    """ポートフォリオのリスク指標を計算するクラス"""

    def __init__(self, portfolio_data: PortfolioData):
        self.portfolio_data = portfolio_data

    def calculate_var(self, confidence_level: float = 0.95) -> float:
        """VaR（Value at Risk）を計算"""
        returns = self.portfolio_data.returns
        var = np.percentile(returns, (1 - confidence_level) * 100)
        return var
