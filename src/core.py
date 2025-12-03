# core.py — Punto central del módulo

from prolongation import prolong
from involution import apply_canonical_involution
from discrepancy import compute_discrepancy

TOL = 1e-8

def check_involution_condition(system, order_k=1):
    """
    Evalúa la condición de involutividad de un sistema diferencial.

    system: diccionario con derivadas y expresiones SymPy
    order_k: orden de prolongación/autoinvolución
    """
    prolonged = prolong(system, order=order_k)
    involuted = apply_canonical_involution(system)
    discrepancy = compute_discrepancy(prolonged, involuted)

    if discrepancy < TOL:
        return True, prolonged
    
    return False, prolonged
