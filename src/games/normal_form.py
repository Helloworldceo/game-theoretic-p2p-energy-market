"""Normal-form games and Nash equilibrium utilities."""

from __future__ import annotations
import numpy as np
from itertools import product


class NormalFormGame:
    """Two-player normal-form game."""

    def __init__(self, payoff_A: np.ndarray, payoff_B: np.ndarray, name: str = ""):
        """
        payoff_A, payoff_B : shape (n_actions_A, n_actions_B)
        """
        self.A = np.asarray(payoff_A, dtype=float)
        self.B = np.asarray(payoff_B, dtype=float)
        self.name = name
        assert self.A.shape == self.B.shape

    @property
    def n_actions(self):
        return self.A.shape

    def pure_nash(self):
        """Find all pure-strategy Nash equilibria."""
        n, m = self.A.shape
        equilibria = []
        for i, j in product(range(n), range(m)):
            # Best response for A
            if self.A[i, j] < np.max(self.A[:, j]):
                continue
            # Best response for B
            if self.B[i, j] < np.max(self.B[i, :]):
                continue
            equilibria.append((i, j))
        return equilibria

    def best_response_A(self, strategy_B):
        """Best response of A to a mixed strategy of B."""
        expected = self.A @ strategy_B
        return np.argmax(expected)

    def best_response_B(self, strategy_A):
        expected = strategy_A @ self.B
        return np.argmax(expected)


def prisoners_dilemma():
    # Cooperate = 0, Defect = 1
    A = np.array([[3, 0],
                  [5, 1]])
    B = np.array([[3, 5],
                  [0, 1]])
    return NormalFormGame(A, B, name="Prisoner's Dilemma")


def coordination_game():
    A = np.array([[2, 0],
                  [0, 1]])
    B = A.copy()
    return NormalFormGame(A, B, name="Coordination Game")


def battle_of_sexes():
    A = np.array([[2, 0],
                  [0, 1]])
    B = np.array([[1, 0],
                  [0, 2]])
    return NormalFormGame(A, B, name="Battle of the Sexes")
