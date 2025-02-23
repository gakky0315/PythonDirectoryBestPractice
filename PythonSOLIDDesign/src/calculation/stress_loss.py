import pandas as pd
from src.data.stress_test_data import StressTestData
from abc import ABC, abstractmethod

class AbstractStressLossCalculator(ABC):
    """ストレスロス計算の抽象クラス"""

    @abstractmethod
    def calculate_stress_loss(self, stress_data: StressTestData) -> pd.Series:
        pass

class StressLossCalculator(AbstractStressLossCalculator):
    """ストレスロス計算を行うクラス"""

    def calculate_stress_loss(self, stress_data: StressTestData) -> pd.Series:
        """ストレスシナリオに基づく損失を計算"""
        return stress_data.shock_factors.sum(axis=1) * stress_data.stress_losses
