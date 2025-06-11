"""
QuantFlow: Essential quantitative finance tools for modern portfolio management.

A comprehensive Python package for options pricing, risk analytics, and market data processing.
"""

__version__ = "0.1.6"
__author__ = "JEEVAN B A"
__email__ = "jeevanba273@gmail.com"

# Import main classes for easy access
from .options.black_scholes import BlackScholes
from .risk.metrics import RiskMetrics
from .data.fetcher import MarketData

__all__ = ['BlackScholes', 'RiskMetrics', 'MarketData']