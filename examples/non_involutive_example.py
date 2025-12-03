# non_involutive_example.py
import os, sys
# Añadir automáticamente la ruta del proyecto (sube desde /src/examples/ a /src/)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import check_involution_condition
import sympy as sp

# Ejemplo NO involutivo:
# u_x = y'(x)
# u   = y(x)^2

x = sp.Symbol("x")
y = sp.Function("y")(x)
p = sp.diff(y, x)

# Sistema no involutivo
system = {
    "u_x": p,       # y'
    "u": y**2       # y^2
}

print("Checking involution of NON-INVOLUTIVE system: u_x = y', u = y^2")
result = check_involution_condition(system, order_k=1)
print(result)
