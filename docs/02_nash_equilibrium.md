# Nash Equilibrium

## Definition

A strategy profile is a **Nash equilibrium** if no player can improve their own payoff by unilaterally changing their strategy, assuming the others keep theirs fixed.

In other words: every player is playing a **best response** to the others.

## Pure vs Mixed

- **Pure-strategy Nash**: each player chooses one action with probability 1.
- **Mixed-strategy Nash**: players randomize over actions. This is needed when no pure equilibrium exists (or to describe equilibria in which players are indifferent).

## How we find them in small games

1. For pure equilibria: check every cell of the payoff matrix; keep the cells where the row player’s payoff is maximal in its column **and** the column player’s payoff is maximal in its row.
2. For 2×2 mixed equilibria: solve for the probabilities that make the opponent indifferent between their two actions.

The code in `src/games/` implements both checks for the classic examples.

## Important intuition

Nash equilibrium does **not** mean the outcome is socially optimal (Prisoner’s Dilemma is the classic counter-example). It only means that no one has a unilateral incentive to deviate.
