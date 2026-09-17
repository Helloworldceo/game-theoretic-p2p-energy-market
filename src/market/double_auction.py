"""Simple double auction clearing."""

from __future__ import annotations
import numpy as np
from typing import List, Tuple
from .agents import Prosumer


def clear_double_auction(agents: List[Prosumer]) -> Tuple[float, list]:
    """
    Collect bids/offers, find a uniform clearing price, match quantity.

    Returns
    -------
    clearing_price : float
    trades : list of (seller, buyer, quantity, price)
    """
    offers = []  # (price, qty, agent_idx)  qty > 0
    bids = []    # (price, qty, agent_idx)  qty < 0

    for i, a in enumerate(agents):
        qty, price = a.bid()
        if qty > 0.05:
            offers.append((price, qty, i))
        elif qty < -0.05:
            bids.append((price, -qty, i))  # store positive demand

    # Sort offers ascending (cheapest first), bids descending (highest willingness)
    offers.sort(key=lambda x: x[0])
    bids.sort(key=lambda x: -x[0])

    trades = []
    clearing_price = None
    oi, bi = 0, 0
    while oi < len(offers) and bi < len(bids):
        op, oq, oi_idx = offers[oi]
        bp, bq, bi_idx = bids[bi]
        if op > bp:
            break  # no more mutually beneficial trades

        qty = min(oq, bq)
        price = 0.5 * (op + bp)  # mid-point pricing
        clearing_price = price if clearing_price is None else clearing_price

        trades.append((oi_idx, bi_idx, qty, price))

        offers[oi] = (op, oq - qty, oi_idx)
        bids[bi] = (bp, bq - qty, bi_idx)

        if offers[oi][1] < 1e-6:
            oi += 1
        if bids[bi][1] < 1e-6:
            bi += 1

    return clearing_price if clearing_price is not None else 0.0, trades
