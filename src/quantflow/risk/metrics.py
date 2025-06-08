"""
Portfolio risk metrics and analytics.

This module provides implementations of common risk measures including
Value at Risk (VaR), Expected Shortfall, and performance ratios.
"""

import numpy as np
import pandas as pd
from scipy import stats


class RiskMetrics:
    """
    Portfolio risk analysis tools.
    
    Parameters:
    returns: pandas Series or numpy array of portfolio returns
    """
    
    def __init__(self, returns):
        if isinstance(returns, pd.DataFrame):
            # If DataFrame, take the first column or flatten
            self.returns = returns.iloc[:, 0].dropna()
        elif isinstance(returns, pd.Series):
            self.returns = returns.dropna()
        else:
            # Handle numpy arrays
            returns_flat = np.array(returns).flatten()
            self.returns = pd.Series(returns_flat).dropna()
    
    def var_historical(self, confidence_level=0.05):
        """Calculate Historical Value at Risk."""
        return np.percentile(self.returns, confidence_level * 100)
    
    def sharpe_ratio(self, risk_free_rate=0.02):
        """Calculate Sharpe ratio (assuming daily returns)."""
        excess_return = self.returns.mean() - risk_free_rate / 252
        return excess_return / self.returns.std() * np.sqrt(252)
    
    def expected_shortfall(self, confidence_level=0.05):
        """Calculate Expected Shortfall (Conditional VaR)."""
        var = self.var_historical(confidence_level)
        # Average of returns that are worse than VaR
        return self.returns[self.returns <= var].mean()
    
    def max_drawdown(self):
        """Calculate maximum drawdown."""
        # Convert returns to cumulative wealth
        cumulative = (1 + self.returns).cumprod()
        rolling_max = cumulative.expanding().max()
        drawdown = (cumulative - rolling_max) / rolling_max
        return drawdown.min()