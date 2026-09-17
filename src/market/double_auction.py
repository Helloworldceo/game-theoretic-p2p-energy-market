"""Double auction with profit accounting."""

from __future__ import annotations
from typing import List, Tuple
from .agents import Prosumer


def clear_double_auction(agents: List[Prosumer]) -> Tuple[float, list, float]:
    """
    Returns clearing_price, list of trades (seller_idx, buyer_idx, qty, price), total_volume.
    Also updates agent.profit.
    """
    offers = []
    bids = []

    for i, a in enumerate(agents):
        qty, price = a.bid()
        if qty > 0.05:
            offers.append([price, qty, i])
        elif qty < -0.05:
            bids.append([price, -qty, i])

    offers.sort(key=lambda x: x[0])
    bids.sort(key=lambda x: -x[0])

    trades = []
    volume = 0.0
    clearing_price = 0.0
    oi = bi = 0

    while oi < len(offers) and bi < len(bids):
        op, oq, si = offers[oi]
        bp, bq, bi_idx = bids[bi]
        if op > bp:
            break
        qty = min(oq, bq)
        price = 0.5 * (op + bp)
        clearing_price = price
        trades.append((si, bi_idx, qty, price))
        volume += qty

        # Profit: seller receives price*qty, buyer pays price*qty
        agents[si].profit += price * qty
        agents[bi_idx].profit -= price * qty

        offers[oi][1] -= qty
        bids[bi][1] -= qty
        if offers[oi][1] < 1e-6:
            oi += 1
        if bids[bi][1] < 1e-6:
            bi += 1

    return clearing_price, trades, volume
