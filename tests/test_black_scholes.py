"""
Test the Black-Scholes implementation.
"""

import sys
import os

# Add the src folder to Python path so we can import our code
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from quantflow.options.black_scholes import BlackScholes


def test_basic_call_option():
    """Test a basic call option price."""
    # Create a call option: Stock=$100, Strike=$100, 1 year, 5% rate, 20% volatility
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    price = option.price()
    
    print(f"Call option price: ${price:.2f}")
    
    # The theoretical price should be around $10.45
    assert 10.0 < price < 11.0, f"Price {price} seems wrong for this call option"
    print("✓ Call option test passed!")

def test_delta_calculation():
    """Test delta calculation."""
    # Same option as before
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    delta = option.delta()
    
    print(f"Call option delta: {delta:.3f}")
    
    # Delta for ATM call should be around 0.6
    assert 0.55 < delta < 0.65, f"Delta {delta} seems wrong"
    print("✓ Delta test passed!")

def test_gamma_calculation():
    """Test gamma calculation."""
    # Same option as before
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    gamma = option.gamma()
    
    print(f"Call option gamma: {gamma:.4f}")
    
    # Gamma for ATM options should be around 0.02
    assert 0.015 < gamma < 0.025, f"Gamma {gamma} seems wrong"
    print("✓ Gamma test passed!")

def test_theta_calculation():
    """Test theta calculation."""
    # Same option as before
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    theta = option.theta()
    
    print(f"Call option theta: ${theta:.2f} per year")
    print(f"Daily theta: ${theta/365:.3f} per day")
    
    # Theta should be negative for long options (time decay)
    assert theta < 0, f"Theta {theta} should be negative for long options"
    assert -10 < theta < -1, f"Theta {theta} seems out of reasonable range"
    print("✓ Theta test passed!")


def test_vega_calculation():
    """Test vega calculation."""
    # Same option as before
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    vega = option.vega()
    
    print(f"Call option vega: ${vega:.2f} per 1% volatility change")
    
    # Vega should be positive (higher volatility = higher option value)
    assert vega > 0, f"Vega {vega} should be positive"
    assert 0.2 < vega < 0.6, f"Vega {vega} seems out of reasonable range"
    print("✓ Vega test passed!")

def test_greeks_summary():
    """Test the convenient Greeks summary function."""
    option = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    greeks = option.greeks()
    
    print("\n📊 Complete Greeks Summary:")
    print(f"Price: ${greeks['price']:.2f}")
    print(f"Delta: {greeks['delta']:.3f}")
    print(f"Gamma: {greeks['gamma']:.4f}")
    print(f"Theta: ${greeks['theta']:.2f}")
    print(f"Vega: ${greeks['vega']:.2f}")
    
    # Check that all values are present
    assert 'price' in greeks
    assert 'delta' in greeks
    assert 'gamma' in greeks
    assert 'theta' in greeks
    assert 'vega' in greeks
    print("✓ Greeks summary test passed!")


if __name__ == "__main__":
    test_basic_call_option()
    test_delta_calculation()
    test_gamma_calculation()
    test_theta_calculation()
    test_vega_calculation()
    test_greeks_summary()
    print("All tests passed! 🎉")