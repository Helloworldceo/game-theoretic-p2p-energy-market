"""Simple mixed-strategy Nash helpers for 2x2 games."""

import numpy as np
from .normal_form import NormalFormGame


def mixed_nash_2x2(game: NormalFormGame):
    """
    Analytic mixed Nash for 2x2 games (when it exists).
    Returns (p, q) where p = Prob(A plays action 0), q = Prob(B plays action 0).
    """
    A = game.A
    B = game.B

    # For player B to mix, A must make B indifferent
    # p * B00 + (1-p)*B10 = p * B01 + (1-p)*B11
    denom_B = (B[0, 0] - B[1, 0] - B[0, 1] + B[1, 1])
    if abs(denom_B) < 1e-9:
        return None  # no interior mixed
    p = (B[1, 1] - B[1, 0]) / denom_B

    denom_A = (A[0, 0] - A[0, 1] - A[1, 0] + A[1, 1])
    if abs(denom_A) < 1e-9:
        return None
    q = (A[1, 1] - A[0, 1]) / denom_A

    if 0 < p < 1 and 0 < q < 1:
        return p, q
    return None
