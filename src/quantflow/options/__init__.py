"""
Options pricing and Greeks calculation module.

This module provides implementations of various option pricing models including
the Black-Scholes-Merton model for European options.
"""

from .black_scholes import BlackScholes

__all__ = ['BlackScholes']