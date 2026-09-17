# Game-Theoretic Peer-to-Peer Energy Market

Simulation of strategic interactions among prosumers in a local electricity market.

## Features

- Classic normal-form games + pure & mixed Nash solvers
- Multi-prosumer P2P market with double auction
- Agent profit tracking and strategy comparison
- Stackelberg (leader-follower) pricing example
- Market efficiency & volume metrics
- Time-series plots of clearing price and traded volume
- Clean, modular Python code

## Quick Start

```bash
git clone https://github.com/Helloworldceo/game-theoretic-p2p-energy-market.git
cd game-theoretic-p2p-energy-market
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m src.main
```

Plots are saved to `results/`.

## Key Concepts Demonstrated

- Nash equilibrium (pure & mixed)
- Dominant strategies
- Double auction market clearing
- Stackelberg leadership
- Effect of bidding strategy on profit and market efficiency
