"""
Test the market data implementation.
"""

import sys
import os

# Add the src folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from quantflow.data.fetcher import MarketData


def test_single_stock_fetch():
    """Test fetching data for a single stock."""
    print("📈 Fetching AAPL data...")
    
    # Fetch Apple stock data for 6 months
    data = MarketData.fetch_stock_data('AAPL', period='6mo')
    
    print(f"Data shape: {data.shape}")
    print(f"Date range: {data.index[0].date()} to {data.index[-1].date()}")
    print(f"Latest price: ${data.iloc[-1, 0]:.2f}")
    
    # Check that we got reasonable data
    assert len(data) > 100, f"Expected more data points, got {len(data)}"
    assert data.iloc[-1, 0] > 0, "Stock price should be positive"
    print("✓ Single stock fetch test passed!")


def test_returns_calculation():
    """Test returns calculation."""
    print("\n📊 Testing returns calculation...")
    
    # Fetch data and calculate returns
    data = MarketData.fetch_stock_data('MSFT', period='3mo')
    returns = MarketData.calculate_returns(data)
    
    print(f"Returns data shape: {returns.shape}")
    print(f"Average daily return: {returns.mean().iloc[0]:.4f} ({returns.mean().iloc[0]*100:.2f}%)")
    print(f"Daily volatility: {returns.std().iloc[0]:.4f} ({returns.std().iloc[0]*100:.2f}%)")
    
    # Check returns are reasonable
    assert len(returns) == len(data) - 1, "Returns should have one less observation than prices"
    assert not returns.isna().any().any(), "Returns should not contain NaN values"
    print("✓ Returns calculation test passed!")


if __name__ == "__main__":
    test_single_stock_fetch()
    test_returns_calculation()
    print("\nAll market data tests passed! 🎉")