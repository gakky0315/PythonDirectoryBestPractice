from setuptools import setup, find_packages

setup(
    name="ArithmeticOperations",
    version="0.1.0",
    description="A Python project for arithmetic operations",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
    ],
)
