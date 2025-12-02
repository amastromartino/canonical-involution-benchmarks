# basic_benchmarks.py
"""
Benchmarks básicos para canonical-involution-benchmarks.

Mide:
- Tiempo de prolongación
- Tiempo de aplicación de involución
- Tiempo de cómputo de discrepancia

Estos benchmarks no requieren datos externos.
"""

import time
import sympy as sp

from prolongation import prolong
from involution import apply_canonical_involution
from discrepancy import compute_discrepancy

# Variables simbólicas
x, y = sp.symbols("x y")
u = sp.Function("u")(x, y)

# Sistema simple de prueba
system = {
    "u_x": u.diff(x),
    "u_y": u.diff(y),
}

def benchmark_prolongation():
    start = time.time()
    out = prolong(system)
    elapsed = time.time() - start
    return elapsed, out

def benchmark_involution():
    start = time.time()
    out = apply_canonical_involution(prolong(system))
    elapsed = time.time() - start
    return elapsed, out

def benchmark_discrepancy():
    p = prolong(system)
    i = apply_canonical_involution(p)
    start = time.time()
    out = compute_discrepancy(p, i)
    elapsed = time.time() - start
    return elapsed, out

if __name__ == "__main__":
    print("=== CANONICAL INVOLUTION BENCHMARKS ===\n")

    t1, p = benchmark_prolongation()
    print(f"Prolongation time: {t1:.6f} s")
    print(f"Prolonged system: {p}\n")

    t2, inv = benchmark_involution()
    print(f"Involution time: {t2:.6f} s")
    print(f"Involuted system: {inv}\n")

    t3, disc = benchmark_discrepancy()
    print(f"Discrepancy time: {t3:.6f} s")
    print(f"Discrepancy result: {disc}\n")

    print("Benchmarks completed.")
