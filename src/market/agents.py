"""Prosumer agents for the P2P market."""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass


@dataclass
class Prosumer:
    name: str
    pv: float                 # current generation (kW)
    load: float               # current demand (kW)
    battery_soc: float = 0.5
    battery_capacity: float = 5.0
    max_buy_price: float = 0.25
    min_sell_price: float = 0.08

    @property
    def net(self):
        """Positive = surplus (wants to sell), negative = deficit (wants to buy)."""
        return self.pv - self.load

    def bid(self):
        """
        Simple bidding strategy.
        Returns (quantity, price) where quantity > 0 means sell offer,
        quantity < 0 means buy bid.
        """
        net = self.net
        if net > 0.1:  # surplus
            # Willing to sell, price between min_sell and a bit higher
            price = self.min_sell_price + 0.02 * np.random.rand()
            qty = net * 0.8   # keep some for self
            return qty, price
        elif net < -0.1:  # deficit
            price = self.max_buy_price - 0.03 * np.random.rand()
            qty = net        # negative
            return qty, price
        else:
            return 0.0, 0.0
