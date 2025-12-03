import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import check_involution_condition

import sympy as sp

# Ejemplo NO involutivo: y' = x^2, u = y'(x)^2

x = sp.Symbol("x")
y = sp.Function("y")(x)
p = sp.diff(y, x)

system = {
    "u_x": p,           # ecuación para y'
    "u": p**2 + x       # ecuación incompatible → NO involutiva
}

print("Checking non-involutive example...")
result = check_involution_condition(system, order_k=1)
print(result)

