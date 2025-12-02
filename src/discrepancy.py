# discrepancy.py
import sympy as sp

def compute_discrepancy(sys1, sys2):
    """
    Computes symbolic discrepancy Δ = sys1 - sys2.
    If Δ is identically zero, the system is holonomic/in involution.
    """

    discrepancy = {}

    for key in sys1:
        if key in sys2:
            discrepancy[key] = sp.simplify(sys1[key] - sys2[key])

    return discrepancy
