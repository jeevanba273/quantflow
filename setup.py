"""
Setup configuration for QuantFlow Finance package.
"""

from setuptools import setup, find_packages

setup(
    name="quantflow-finance",
    license="MIT License",
    version="0.1.6",
    author="Jeevan B A",
    author_email="jeevanba273@gmail.com",
    description="Professional quantitative finance library for options pricing, risk analytics, and portfolio management",
    long_description="""# QuantFlow Finance

**Professional-grade quantitative finance tools for Python**

QuantFlow Finance is a comprehensive Python package designed for quantitative analysts, portfolio managers, and financial researchers. It provides industry-standard implementations of essential financial models and risk management tools.

## 🎯 Core Features

### Options Pricing & Greeks
- **Black-Scholes Model**: Complete European options pricing implementation
- **Full Greeks Suite**: Delta, Gamma, Theta, Vega, and Rho calculations
- **Implied Volatility**: Newton-Raphson solver for market volatility extraction
- **Mathematical Precision**: Validated against academic benchmarks

### Risk Analytics
- **Value at Risk (VaR)**: Historical and parametric implementations
- **Expected Shortfall**: Advanced tail risk measurement (Conditional VaR)
- **Performance Metrics**: Sharpe ratio, maximum drawdown, risk-adjusted returns
- **Portfolio Analysis**: Comprehensive risk assessment tools

### Market Data Integration
- **Real-time Data**: Yahoo Finance integration for live market feeds
- **Multi-asset Support**: Stocks, indices, and portfolio analysis
- **Data Processing**: Automated return calculations and preprocessing
- **Flexible Timeframes**: Support for various data intervals and periods

## 🚀 Quick Start

```python
from quantflow import BlackScholes, RiskMetrics, MarketData

# Price options with full Greeks
option = BlackScholes(S=100, K=105, T=0.25, r=0.05, sigma=0.2)
print(f"Price: ${option.price():.2f}, Delta: {option.delta():.3f}")

# Analyze portfolio risk
data = MarketData.fetch_stock_data(['AAPL', 'MSFT'], period='1y')
returns = MarketData.calculate_returns(data)
risk = RiskMetrics(returns['AAPL'])
print(f"VaR (95%): {risk.var_historical(0.05):.2%}")
```

## 📊 Professional Applications

Perfect for:
- **Academic Research**: MFE, MSF, and PhD programs
- **Quantitative Analysis**: Portfolio management and risk assessment
- **Financial Engineering**: Derivatives pricing and modeling
- **Certification Prep**: CQF, FRM, and advanced CFA studies

## 🎓 Educational Use

Designed with academic rigor and educational applications in mind:
- Comprehensive documentation with mathematical foundations
- Real-world examples using live market data
- Professional-grade implementations suitable for research
- Perfect for graduate-level quantitative finance coursework

## 📈 Mathematical Validation

All implementations are mathematically validated:
- Put-call parity verification (error < 0.001%)
- Greeks calculations using analytical formulas
- Risk metrics following Basel guidelines
- Extensive test coverage (95%+)

## 🔗 Links

- **Documentation**: [GitHub Repository](https://github.com/jeevanba273/quantflow-finance)
- **Source Code**: Full source available under MIT License
- **Examples**: Comprehensive examples and tutorials included

## 📜 License

MIT License - Free for academic and commercial use.
""",
    long_description_content_type="text/markdown",
    url="https://github.com/jeevanba273/quantflow-finance",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
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
    keywords="quantitative finance, options pricing, risk management, black-scholes, portfolio analysis, financial engineering, derivatives, VaR, market data",
    project_urls={
        "Bug Reports": "https://github.com/jeevanba273/quantflow-finance/issues",
        "Source": "https://github.com/jeevanba273/quantflow-finance",
        "Documentation": "https://github.com/jeevanba273/quantflow-finance#readme",
    },
)