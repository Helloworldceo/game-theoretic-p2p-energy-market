"""Stackelberg pricing example."""

import numpy as np


def follower_best_response(price: float, preferred: float = 2.2, discomfort: float = 0.6):
    q = preferred - price / (2 * discomfort)
    return max(0.05, q)


def leader_payoff(price: float, n_followers: int = 6):
    total_demand = sum(follower_best_response(price) for _ in range(n_followers))
    revenue = price * total_demand
    cost = 0.08 * price ** 2
    return revenue - cost, total_demand


def find_stackelberg_equilibrium(price_grid=None):
    if price_grid is None:
        price_grid = np.linspace(0.04, 0.45, 42)
    best_p, best_pay, best_d = None, -np.inf, 0
    for p in price_grid:
        pay, dem = leader_payoff(p)
        if pay > best_pay:
            best_p, best_pay, best_d = p, pay, dem
    return best_p, best_pay, best_d
