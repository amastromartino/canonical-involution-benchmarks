from core import check_involution_condition
import sympy as sp

if __name__ == "__main__":
    print("Running involution check...")

    x = sp.Symbol("x")
    y = sp.Function("y")(x)
    p = sp.diff(y, x)

    example_system = {"u_x": p, "u": y}

    result = check_involution_condition(example_system)
    print(result)

