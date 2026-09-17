"""Prosumer agents with different bidding strategies."""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field


@dataclass
class Prosumer:
    name: str
    pv_capacity: float = 4.0
    load_base: float = 2.0
    battery_soc: float = 0.5
    battery_capacity: float = 5.0
    max_buy_price: float = 0.28
    min_sell_price: float = 0.07
    strategy: str = "honest"          # honest | aggressive | conservative
    profit: float = 0.0
    pv: float = 0.0
    load: float = 0.0

    @property
    def net(self) -> float:
        return self.pv - self.load

    def update_profile(self, hour: int, rng: np.random.Generator):
        daylight = max(0.0, np.sin(np.pi * (hour - 6) / 12))
        self.pv = daylight * self.pv_capacity * (0.85 + 0.3 * rng.random())
        self.load = self.load_base * (0.75 + 0.5 * rng.random())
        # evening peak
        if 17 <= hour <= 21:
            self.load *= 1.35

    def bid(self):
        net = self.net
        if net > 0.15:  # seller
            if self.strategy == "aggressive":
                price = self.min_sell_price * 0.9
            elif self.strategy == "conservative":
                price = self.min_sell_price * 1.4
            else:
                price = self.min_sell_price + 0.03 * np.random.rand()
            qty = net * 0.85
            return qty, price
        elif net < -0.15:  # buyer
            if self.strategy == "aggressive":
                price = self.max_buy_price * 1.1
            elif self.strategy == "conservative":
                price = self.max_buy_price * 0.75
            else:
                price = self.max_buy_price - 0.04 * np.random.rand()
            return net, price
        return 0.0, 0.0
