"""Full demonstration with plots."""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from src.games.normal_form import prisoners_dilemma, coordination_game, battle_of_sexes
from src.games.nash import mixed_nash_2x2
from src.market.simulation import run_market_day
from src.stackelberg.example import find_stackelberg_equilibrium

RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)


def demo_classic_games():
    print("=== Classic Games & Nash Equilibria ===")
    for game in [prisoners_dilemma(), coordination_game(), battle_of_sexes()]:
        pure = game.pure_nash()
        print(f"\n{game.name}")
        print(f"  Pure Nash: {pure}")
        mixed = mixed_nash_2x2(game)
        if mixed:
            print(f"  Mixed Nash: P(A plays 0)={mixed[0]:.3f}, P(B plays 0)={mixed[1]:.3f}")
        else:
            print("  No interior mixed-strategy Nash")


def demo_market():
    print("\n=== P2P Double-Auction Market (24 h) ===")
    history, agents = run_market_day(n_agents=12, hours=24, seed=42)

    prices = [h["clearing_price"] for h in history]
    volumes = [h["volume"] for h in history]
    active_prices = [p for p in prices if p > 0]

    print(f"Agents: {len(agents)}")
    print(f"Avg clearing price (when trade occurs): {np.mean(active_prices):.3f} $/kWh" if active_prices else "No trades")
    print(f"Total volume: {sum(volumes):.2f} kWh")
    print(f"Total trades: {sum(h['n_trades'] for h in history)}")

    # Profit by strategy
    from collections import defaultdict
    strat_profit = defaultdict(list)
    for a in agents:
        strat_profit[a.strategy].append(a.profit)
    print("\nMean profit by bidding strategy:")
    for s, vals in strat_profit.items():
        print(f"  {s:12s}: {np.mean(vals):+.3f} $")

    # Plots
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    axes[0].step(range(24), prices, where="mid", color="C0")
    axes[0].set_ylabel("Clearing price ($/kWh)")
    axes[0].set_title("P2P Market – Clearing Price & Volume")
    axes[0].grid(True, alpha=0.3)

    axes[1].bar(range(24), volumes, color="C2", alpha=0.8)
    axes[1].set_ylabel("Volume (kWh)")
    axes[1].set_xlabel("Hour of day")
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(RESULTS / "market_day.png", dpi=150)
    print(f"Saved: {RESULTS / 'market_day.png'}")
    plt.close(fig)


def demo_stackelberg():
    print("\n=== Stackelberg Leader-Follower ===")
    price, payoff, demand = find_stackelberg_equilibrium()
    print(f"Optimal leader price : {price:.3f} $/kWh")
    print(f"Leader payoff        : {payoff:.3f}")
    print(f"Resulting demand     : {demand:.2f} kW")


def main():
    demo_classic_games()
    demo_market()
    demo_stackelberg()
    print("\nAll demonstrations finished. See results/ for plots.")


if __name__ == "__main__":
    main()
