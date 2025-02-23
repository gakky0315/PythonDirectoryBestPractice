import pytest
from src.prediction.predictor import print_func

def test_print_func():
    """print_func() が 1 を返すことをテスト"""
    result = print_func()
    assert result == 1
