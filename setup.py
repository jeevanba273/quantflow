"""
Setup configuration for QuantFlow package.
"""

from setuptools import setup, find_packages

setup(
    name="quantflow",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Essential quantitative finance tools for modern portfolio management",
    long_description="A comprehensive Python package for options pricing, risk analytics, and market data processing.",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quantflow",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "matplotlib>=3.3.0",
        "yfinance>=0.1.70",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
    },
)