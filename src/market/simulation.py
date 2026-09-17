"""Multi-hour P2P market simulation with logging."""

from __future__ import annotations
import numpy as np
from .agents import Prosumer
from .double_auction import clear_double_auction


def run_market_day(n_agents: int = 10, hours: int = 24, seed: int = 42):
    rng = np.random.default_rng(seed)
    strategies = ["honest", "aggressive", "conservative"]

    agents = []
    for i in range(n_agents):
        agents.append(Prosumer(
            name=f"A{i}",
            pv_capacity=rng.uniform(0.5, 7.0),
            load_base=rng.uniform(1.2, 3.8),
            max_buy_price=rng.uniform(0.18, 0.32),
            min_sell_price=rng.uniform(0.05, 0.12),
            strategy=strategies[i % 3],
        ))

    history = []
    for h in range(hours):
        for a in agents:
            a.update_profile(h, rng)
        price, trades, volume = clear_double_auction(agents)
        history.append({
            "hour": h,
            "clearing_price": price,
            "volume": volume,
            "n_trades": len(trades),
        })

    return history, agents
