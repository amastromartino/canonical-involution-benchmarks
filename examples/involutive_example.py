# involutive_example.py
import os, sys
# Añadir automáticamente la ruta del proyecto (sube desde /src/examples/ a /src/)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import check_involution_condition
import sympy as sp

# Ejemplo involutivo: (y')^2 + y^2 - 1 = 0

x = sp.Symbol("x")
y = sp.Function("y")(x)
p = sp.diff(y, x)

# Representación del sistema:
#   u_x = p       (derivada)
#   u   = y       (estado)
system = {
    "u_x": p,
    "u": y
}

print("Checking involution of: (y')^2 + y^2 - 1 = 0")
result = check_involution_condition(system, order_k=1)
print(result)

