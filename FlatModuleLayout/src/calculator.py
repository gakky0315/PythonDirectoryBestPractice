from logger import get_logger

def add(a: float, b: float) -> float:
    """加算"""
    return a + b

def subtract(a: float, b: float) -> float:
    """減算"""
    return a - b

def multiply(a: float, b: float) -> float:
    """乗算"""
    return a * b

def divide(a: float, b: float) -> float:
    """除算（ゼロ除算を防ぐ）"""
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b

if __name__ == "__main__":
    logger = get_logger()  # ロガーを取得
    a = add(1, 2)
    logger.info(f"計算結果: {a}")  # ログを出力
    print(1)
