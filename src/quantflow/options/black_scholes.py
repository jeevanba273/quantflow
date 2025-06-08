"""
Black-Scholes option pricing model implementation.
"""

import numpy as np
from scipy.stats import norm


class BlackScholes:
    """
    Black-Scholes option pricing model.
    
    Parameters:
    S: Current stock price
    K: Strike price  
    T: Time to expiration in years
    r: Risk-free interest rate
    sigma: Volatility
    option_type: 'call' or 'put'
    """
    
    def __init__(self, S, K, T, r, sigma, option_type='call'):
        self.S = float(S)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)
        self.option_type = option_type.lower()
    
    def price(self):
        """Calculate option price using Black-Scholes formula."""
        # Calculate d1 and d2 parameters
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        
        if self.option_type == 'call':
            # Call option formula: S*N(d1) - K*e^(-rT)*N(d2)
            return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            # Put option formula: K*e^(-rT)*N(-d2) - S*N(-d1)
            return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        
    def delta(self):
        """Calculate option delta (price sensitivity to stock price)."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        
        if self.option_type == 'call':
            return norm.cdf(d1)
        else:
            return norm.cdf(d1) - 1
    
    def gamma(self):
        """Calculate option gamma (rate of change of delta)."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        
        # Gamma is the same for both calls and puts
        return norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T))
    
    def theta(self):
        """Calculate option theta (time decay per year)."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        
        first_term = -(self.S * norm.pdf(d1) * self.sigma) / (2 * np.sqrt(self.T))
        
        if self.option_type == 'call':
            second_term = -self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            second_term = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
            
        return first_term + second_term
    
    def vega(self):
        """Calculate option vega (sensitivity to volatility change)."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        
        # Vega is the same for both calls and puts
        # Divide by 100 to get sensitivity per 1% volatility change
        return (self.S * norm.pdf(d1) * np.sqrt(self.T)) / 100
    
    def rho(self):
        """
        Calculate option rho (∂V/∂r).
        
        Rho measures the rate of change of option price with respect to 
        the risk-free interest rate.
        
        Returns
        -------
        float
            Option rho (for 1% change in interest rate)
            
        Notes
        -----
        For calls: ρ = KTe^(-rT)N(d₂) / 100
        For puts: ρ = -KTe^(-rT)N(-d₂) / 100
        """
        d2 = self._d2()
        
        if self.option_type == 'call':
            return (self.K * self.T * np.exp(-self.r * self.T) * 
                   norm.cdf(d2)) / 100
        else:
            return -(self.K * self.T * np.exp(-self.r * self.T) * 
                    norm.cdf(-d2)) / 100
    
    def greeks(self):
        """
        Calculate all Greeks at once.
        
        Returns
        -------
        dict
            Dictionary containing all Greeks:
            - delta: Price sensitivity to underlying
            - gamma: Delta sensitivity to underlying  
            - theta: Time decay (per year)
            - vega: Volatility sensitivity (per 1%)
            - rho: Interest rate sensitivity (per 1%)
        """
        return {
            'price': self.price(),
            'delta': self.delta(),
            'gamma': self.gamma(), 
            'theta': self.theta(),
            'vega': self.vega(),
            'rho': self.rho()
        }
    
    