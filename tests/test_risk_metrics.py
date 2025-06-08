"""
Test the risk metrics implementation.
"""

import sys
import os
import numpy as np

# Add the src folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from quantflow.risk.metrics import RiskMetrics


def test_var_calculation():
    """Test Value at Risk calculation."""
    # Create sample returns (daily returns for 1 year)
    np.random.seed(42)  # For reproducible results
    returns = np.random.normal(0.001, 0.02, 252)  # 1% annual return, 20% volatility
    
    risk_metrics = RiskMetrics(returns)
    var_5 = risk_metrics.var_historical(0.05)  # 5% VaR
    
    print(f"5% VaR: {var_5:.4f} ({var_5*100:.2f}%)")
    
    # VaR should be negative (worst 5% of returns)
    assert var_5 < 0, f"VaR should be negative, got {var_5}"
    print("✓ VaR test passed!")


def test_sharpe_ratio():
    """Test Sharpe ratio calculation."""
    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 252)
    
    risk_metrics = RiskMetrics(returns)
    sharpe = risk_metrics.sharpe_ratio(risk_free_rate=0.02)
    
    print(f"Sharpe ratio: {sharpe:.3f}")
    
    # Sharpe ratio should be reasonable (between -2 and 3 for most portfolios)
    assert -2 < sharpe < 3, f"Sharpe ratio {sharpe} seems unreasonable"
    print("✓ Sharpe ratio test passed!")

def test_expected_shortfall():
    """Test Expected Shortfall calculation."""
    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 252)
    
    risk_metrics = RiskMetrics(returns)
    var_5 = risk_metrics.var_historical(0.05)
    es_5 = risk_metrics.expected_shortfall(0.05)
    
    print(f"5% Expected Shortfall: {es_5:.4f} ({es_5*100:.2f}%)")
    print(f"VaR vs ES: VaR={var_5:.4f}, ES={es_5:.4f}")
    
    # Expected Shortfall should be worse (more negative) than VaR
    assert es_5 < var_5, f"Expected Shortfall {es_5} should be worse than VaR {var_5}"
    print("✓ Expected Shortfall test passed!")


def test_max_drawdown():
    """Test Maximum Drawdown calculation."""
    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 252)
    
    risk_metrics = RiskMetrics(returns)
    max_dd = risk_metrics.max_drawdown()
    
    print(f"Maximum Drawdown: {max_dd:.4f} ({max_dd*100:.2f}%)")
    
    # Max drawdown should be negative (loss from peak)
    assert max_dd <= 0, f"Max drawdown should be negative, got {max_dd}"
    print("✓ Max drawdown test passed!")


if __name__ == "__main__":
    test_var_calculation()
    test_sharpe_ratio()
    test_expected_shortfall()
    test_max_drawdown()
    print("All risk metrics tests passed! 🎉")