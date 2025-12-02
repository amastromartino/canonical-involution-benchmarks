from src.main import check_involution_condition
import sympy as sp

# Ejemplo involutivo: (y')^2 + y^2 - 1 = 0

x = sp.Symbol("x")
y = sp.Function("y")(x)
p = sp.diff(y, x)

system = {
    "u_x": p,
    "u": y
}

print("Checking involution of: (y')^2 + y^2 - 1 = 0")
result = check_involution_condition(system, order_k=1)
print(result)
