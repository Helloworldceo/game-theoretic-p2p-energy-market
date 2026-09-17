# P2P Energy Market & Double Auction

## Why markets?

When many prosumers have surplus solar at different times, a local market can improve efficiency: energy is traded peer-to-peer instead of always buying from / selling to the main grid at less favorable prices.

## Double auction (simplified)

1. Each agent submits either a **sell offer** (quantity + minimum price) or a **buy bid** (quantity + maximum price).
2. Offers are sorted by ascending price, bids by descending price.
3. Trades are matched while the highest remaining bid is still above the lowest remaining offer.
4. A clearing price is set (in this project we use the mid-point of the matched bid and offer).

This mechanism is simple, incentive-compatible enough for demonstration, and produces a market-clearing price and traded volume each hour.

## Bidding strategies implemented

- **Honest**: bid/offer close to true valuation.
- **Aggressive**: try to buy higher / sell lower to increase chance of being matched.
- **Conservative**: more cautious prices, may miss some trades but protect margin.

The simulation tracks profit per strategy so you can see which behavior is more successful under the current rules.
