"""
Market data fetching and preprocessing utilities.

This module provides tools for downloading stock data and calculating returns.
"""

import yfinance as yf
import pandas as pd
import numpy as np


class MarketData:
    """
    Market data utilities for fetching and processing financial data.
    """
    
    @staticmethod
    def fetch_stock_data(tickers, period='1y', interval='1d'):
        """
        Fetch stock data from Yahoo Finance.
        
        Parameters:
        tickers: str or list of str - Stock symbols
        period: str - Time period ('1y', '2y', '5y', etc.)
        interval: str - Data interval ('1d', '1wk', '1mo')
        
        Returns:
        pandas DataFrame with adjusted close prices
        """
        if isinstance(tickers, str):
            tickers = [tickers]
        
        data = yf.download(tickers, period=period, interval=interval)
        
        # Handle different data structures from yfinance
        if len(tickers) == 1:
            # Single ticker - data might be a simple DataFrame
            if 'Adj Close' in data.columns:
                return data[['Adj Close']].rename(columns={'Adj Close': tickers[0]})
            else:
                # Fallback to Close if Adj Close not available
                return data[['Close']].rename(columns={'Close': tickers[0]})
        else:
            # Multiple tickers
            if 'Adj Close' in data.columns:
                return data['Adj Close']
            else:
                return data['Close']
    
    @staticmethod
    def calculate_returns(prices, method='simple'):
        """
        Calculate returns from price data.
        
        Parameters:
        prices: pandas DataFrame or Series
        method: str - 'simple' or 'log' returns
        
        Returns:
        pandas DataFrame or Series of returns
        """
        if method == 'simple':
            return prices.pct_change().dropna()
        elif method == 'log':
            return np.log(prices / prices.shift(1)).dropna()
        else:
            raise ValueError("Method must be 'simple' or 'log'")