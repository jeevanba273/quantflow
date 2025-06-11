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
        
        # Validate we have data
        if len(self.returns) == 0:
            raise ValueError("No valid return data provided. Cannot calculate risk metrics.")
        
        # Warn if we have very little data
        if len(self.returns) < 30:
            print(f"Warning: Only {len(self.returns)} data points available. Risk metrics may be unreliable.")
    
    def var_historical(self, confidence_level=0.05):
        """
        Calculate Historical Value at Risk.
        
        Parameters:
        confidence_level: float - Confidence level (e.g., 0.05 for 95% VaR)
        
        Returns:
        float - VaR value (negative number representing loss)
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for VaR calculation")
        
        if not (0 < confidence_level < 1):
            raise ValueError("Confidence level must be between 0 and 1")
        
        return np.percentile(self.returns, confidence_level * 100)
    
    def var_parametric(self, confidence_level=0.05):
        """
        Calculate Parametric VaR (assumes normal distribution).
        
        Parameters:
        confidence_level: float - Confidence level
        
        Returns:
        float - Parametric VaR value
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for parametric VaR calculation")
        
        mean_return = self.returns.mean()
        std_return = self.returns.std()
        z_score = stats.norm.ppf(confidence_level)
        
        return mean_return + z_score * std_return
    
    def sharpe_ratio(self, risk_free_rate=0.02):
        """
        Calculate Sharpe ratio (assuming daily returns).
        
        Parameters:
        risk_free_rate: float - Annual risk-free rate (default 2%)
        
        Returns:
        float - Annualized Sharpe ratio
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for Sharpe ratio calculation")
        
        excess_return = self.returns.mean() - risk_free_rate / 252
        return excess_return / self.returns.std() * np.sqrt(252)
    
    def expected_shortfall(self, confidence_level=0.05):
        """
        Calculate Expected Shortfall (Conditional VaR).
        
        Parameters:
        confidence_level: float - Confidence level
        
        Returns:
        float - Expected Shortfall value
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for Expected Shortfall calculation")
        
        var = self.var_historical(confidence_level)
        # Average of returns that are worse than VaR
        tail_returns = self.returns[self.returns <= var]
        
        if len(tail_returns) == 0:
            # If no returns are worse than VaR, return the VaR itself
            return var
        
        return tail_returns.mean()
    
    def max_drawdown(self):
        """
        Calculate maximum drawdown.
        
        Returns:
        float - Maximum drawdown as a percentage (negative value)
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for maximum drawdown calculation")
        
        # Convert returns to cumulative wealth
        cumulative = (1 + self.returns).cumprod()
        rolling_max = cumulative.expanding().max()
        drawdown = (cumulative - rolling_max) / rolling_max
        return drawdown.min()
    
    def volatility(self, annualized=True):
        """
        Calculate volatility.
        
        Parameters:
        annualized: bool - Whether to annualize the volatility
        
        Returns:
        float - Volatility (standard deviation of returns)
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for volatility calculation")
        
        vol = self.returns.std()
        if annualized:
            vol *= np.sqrt(252)  # Assuming daily returns
        return vol
    
    def information_ratio(self, benchmark_returns):
        """
        Calculate Information Ratio.
        
        Parameters:
        benchmark_returns: array-like - Benchmark returns for comparison
        
        Returns:
        float - Information ratio
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for Information Ratio calculation")
        
        if isinstance(benchmark_returns, (pd.Series, pd.DataFrame)):
            benchmark_returns = benchmark_returns.values.flatten()
        
        # Align lengths
        min_length = min(len(self.returns), len(benchmark_returns))
        portfolio_rets = self.returns.iloc[-min_length:]
        benchmark_rets = benchmark_returns[-min_length:]
        
        excess_returns = portfolio_rets - benchmark_rets
        tracking_error = excess_returns.std()
        
        if tracking_error == 0:
            return 0
        
        return excess_returns.mean() / tracking_error * np.sqrt(252)
    
    def summary_stats(self):
        """
        Calculate comprehensive risk statistics.
        
        Returns:
        dict - Dictionary containing various risk metrics
        """
        if len(self.returns) == 0:
            raise ValueError("No return data available for summary statistics")
        
        return {
            'count': len(self.returns),
            'mean_return': self.returns.mean(),
            'volatility': self.volatility(),
            'sharpe_ratio': self.sharpe_ratio(),
            'var_95': self.var_historical(0.05),
            'var_99': self.var_historical(0.01),
            'expected_shortfall_95': self.expected_shortfall(0.05),
            'max_drawdown': self.max_drawdown(),
            'skewness': self.returns.skew(),
            'kurtosis': self.returns.kurtosis()
        }