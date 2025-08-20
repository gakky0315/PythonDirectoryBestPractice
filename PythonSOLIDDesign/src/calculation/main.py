from src.data.data_loader import DataLoader
from src.calculation.allocation import AllocationCalculator
from src.calculation.risk_metrics import RiskMetrics
from src.calculation.stress_loss import StressLossCalculator
from src.data.stress_test_data import StressTestData

# CSVファイルを読み込む場合
file_path = "data/portfolio.csv"

data_loader    = DataLoader(file_path)
portfolio_data = data_loader.load_csv()

print("data:")
print(portfolio_data.head())

# JSONファイルを読み込む場合
json_loader = DataLoader("data/portfolio.json")
portfolio_data_json = json_loader.load_json()

print("JSON:")
print(portfolio_data_json.head())

x=1+2
y = x + 1

# アロケーション計算
alloc_calc = AllocationCalculator(portfolio_data)
allocations = alloc_calc.calculate_allocation()
print("Allocations:", allocations)

# リスク指標計算
risk_metrics = RiskMetrics(portfolio_data)
var = risk_metrics.calculate_var()
print("VaR:", var)

# ストレスロス計算
stress_test_data = StressTestData("Crisis", shock_factors, stress_losses)
stress_calc = StressLossCalculator()
stress_loss = stress_calc.calculate_stress_loss(stress_test_data)
print("Stress Loss:", stress_loss)