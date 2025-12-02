# discrepancy.py
import sympy as sp

def compute_discrepancy(sys1, sys2):
    """
    Compara ambos sistemas clave por clave.
    Si una clave falta, su valor se toma como 0.
    """
    keys = set(sys1.keys()) | set(sys2.keys())
    delta = {}

    for k in keys:
        v1 = sys1.get(k, 0)
        v2 = sys2.get(k, 0)
        delta[k] = float(sp.simplify(v1 - v2))

    return delta

