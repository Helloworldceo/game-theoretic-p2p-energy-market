"""Run demonstrations of all major components."""

from src.games.normal_form import prisoners_dilemma, coordination_game, battle_of_sexes
from src.games.nash import mixed_nash_2x2
from src.market.simulation import run_market_day
from src.stackelberg.example import find_stackelberg_equilibrium


def demo_classic_games():
    print("=== Classic Games ===")
    for game in [prisoners_dilemma(), coordination_game(), battle_of_sexes()]:
        pure = game.pure_nash()
        print(f"\n{game.name}")
        print(f"  Pure Nash equilibria (row, col): {pure}")
        mixed = mixed_nash_2x2(game)
        if mixed:
            print(f"  Mixed Nash: P(A=0)={mixed[0]:.3f}, P(B=0)={mixed[1]:.3f}")
        else:
            print("  No interior mixed Nash")


def demo_market():
    print("\n=== P2P Double Auction Market (one day) ===")
    history, agents = run_market_day(n_agents=8, hours=24)
    prices = [h["clearing_price"] for h in history if h["clearing_price"] > 0]
    volumes = [h["volume"] for h in history]
    print(f"Average clearing price: {sum(prices)/len(prices):.3f} $/kWh" if prices else "No trades")
    print(f"Total volume traded: {sum(volumes):.2f} kWh")
    print(f"Number of agents: {len(agents)}")


def demo_stackelberg():
    print("\n=== Stackelberg Example ===")
    price, payoff, demand = find_stackelberg_equilibrium()
    print(f"Leader optimal price: {price:.3f} $/kWh")
    print(f"Leader payoff: {payoff:.3f}")
    print(f"Total follower demand: {demand:.2f} kW")


def main():
    demo_classic_games()
    demo_market()
    demo_stackelberg()
    print("\nAll demonstrations finished.")


if __name__ == "__main__":
    main()
