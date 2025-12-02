# prolongation.py
import sympy as sp

def prolong(system, order=1):
    """
    Basic symbolic prolongation operator.
    Given a first-order system {u_x, u_y}, this adds second-order mixed derivatives.
    This is a simplified version consistent with the article's examples.
    """

    new_sys = {}

    for key, expr in system.items():
        new_sys[key] = expr

        # Extract variable from key name u_x, u_y
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
