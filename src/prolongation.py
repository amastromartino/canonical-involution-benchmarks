# prolongation.py
import sympy as sp

def prolong(system, order=1):
    """
    Basic symbolic prolongation operator.
    If the system is numeric (floats), prolongation is skipped.
    """
    new_sys = {}

    for key, expr in system.items():
        new_sys[key] = expr

    # Detectar si el sistema es simbólico
    symbolic_mode = any(hasattr(expr, "diff") for expr in system.values())

    if not symbolic_mode:
        # No intentar prolongar sistemas numéricos
        return new_sys

    # ---- Prolongación solo para sistemas simbólicos ----
    for key, expr in system.items():
        if "_" not in key:
            continue

        var = key.split("_")[1]

        if var == "x":
            new_sys["u_xx"] = expr.diff(sp.Symbol("x"))
            new_sys["u_xy"] = expr.diff(sp.Symbol("y"))

        if var == "y":
            new_sys["u_yy"] = expr.diff(sp.Symbol("y"))
            new_sys["u_yx"] = expr.diff(sp.Symbol("x"))

    return new_sys
