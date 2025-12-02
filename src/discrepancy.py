# discrepancy.py
import sympy as sp

def compute_discrepancy(sys1, sys2):
    """
    Computes symbolic discrepancy Δ = sys1 - sys2.
    If Δ is identically zero, the system is holonomic/in involution.
    """
    delta = {}

    for key in sys1:
        if key in sys2:
            delta[key] = sp.simplify(sys1[key] - sys2[key])

    return delta
