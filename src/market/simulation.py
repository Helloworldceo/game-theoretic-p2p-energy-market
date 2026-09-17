"""Run a multi-period P2P market simulation."""

from __future__ import annotations
import numpy as np
from .agents import Prosumer
from .double_auction import clear_double_auction


def run_market_day(n_agents: int = 6, hours: int = 24, seed: int = 42):
    rng = np.random.default_rng(seed)

    agents = []
    for i in range(n_agents):
        # Mix of pure consumers, pure producers, prosumers
        pv_peak = rng.uniform(0, 6)
        load_base = rng.uniform(1.0, 3.5)
        agents.append(Prosumer(
            name=f"Agent-{i}",
            pv=0.0,
            load=load_base,
            max_buy_price=rng.uniform(0.18, 0.30),
            min_sell_price=rng.uniform(0.05, 0.12),
        ))

    history = []
    for h in range(hours):
        # Update PV (simple daylight pattern)
        daylight = max(0, np.sin(np.pi * (h - 6) / 12))
        for a in agents:
            a.pv = a.pv * 0  # reset
            # Each agent has its own PV size stored implicitly via initial random
            # For simplicity we re-draw a scaled profile
            a.pv = daylight * rng.uniform(0, 5)
            a.load = a.load * (0.9 + 0.2 * rng.random())  # small variation

        price, trades = clear_double_auction(agents)
        total_traded = sum(t[2] for t in trades)
        history.append({
            "hour": h,
            "clearing_price": price,
            "volume": total_traded,
            "n_trades": len(trades),
        })

    return history, agents
