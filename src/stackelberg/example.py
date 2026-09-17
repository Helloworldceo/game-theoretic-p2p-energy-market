"""
Simple Stackelberg example in an energy context.

Leader = Aggregator / utility that sets a price signal.
Followers = Prosumers that best-respond with their consumption / battery action.
"""

import numpy as np


def follower_best_response(price: float, load_pref: float = 2.0, discomfort_coef: float = 0.5):
    """
    Follower solves a simple quadratic utility maximization:
    max  load_pref * q - discomfort_coef * (q - preferred)^2 - price * q
    """
    preferred = load_pref
    # Analytic solution of the quadratic
    q = preferred - (price) / (2 * discomfort_coef)
    return max(0.1, q)


def leader_payoff(price: float, n_followers: int = 5):
    """Leader revenue minus a cost of high prices (e.g. regulation / churn)."""
    total_demand = sum(follower_best_response(price) for _ in range(n_followers))
    revenue = price * total_demand
    cost = 0.1 * price ** 2   # soft penalty on high prices
    return revenue - cost, total_demand


def find_stackelberg_equilibrium(price_grid=None):
    if price_grid is None:
        price_grid = np.linspace(0.05, 0.40, 36)
    best_price = None
    best_payoff = -np.inf
    best_demand = 0
    for p in price_grid:
        payoff, demand = leader_payoff(p)
        if payoff > best_payoff:
            best_payoff = payoff
            best_price = p
            best_demand = demand
    return best_price, best_payoff, best_demand
