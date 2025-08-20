from setuptools import setup, find_packages

setup(
    name="acme.sql",
    version="0.1.1",  # ★ここでバージョンを定義
    description="A sample SQL utility package",
    author="Your Name",
    packages=find_packages(),  # acme/ を自動検出
    python_requires=">=3.7",
)