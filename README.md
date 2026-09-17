# Game-Theoretic Peer-to-Peer Energy Market

Complete project simulating strategic interactions among prosumers in a local electricity market.

## Features

- Classic normal-form games (Prisoner's Dilemma, Coordination, Battle of the Sexes)
- Algorithms to find pure and mixed Nash equilibria in small games
- Multi-prosumer energy market environment
- Double auction mechanism
- Stackelberg (leader-follower) example
- Simple multi-agent learning demonstration
- Metrics: market efficiency, agent profits, renewable utilization, price volatility

## Quick Start

```bash
git clone https://github.com/Helloworldceo/game-theoretic-p2p-energy-market.git
cd game-theoretic-p2p-energy-market
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m src.main
```

## Structure

```
src/
├── games/               # Classic games + Nash solvers
├── market/              # P2P market, auction, agents
├── stackelberg/
└── main.py
```
