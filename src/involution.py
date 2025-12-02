# involution.py
import sympy as sp

def apply_canonical_involution(system, order_k=1):
    """
    Canonical involution α^{(k)}_θ.
    Symmetrizes mixed derivatives u_xy and u_yx.
    """

    involuted = {}

    for key, expr in system.items():
        if key in ("u_xy", "u_yx"):
            avg = (system.get("u_xy", 0) + system.get("u_yx", 0)) / 2
            involuted["u_xy"] = avg
            involuted["u_yx"] = avg
        else:
            involuted[key] = expr

    return involuted
