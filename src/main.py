# main.py

from prolongation import prolong
from involution import apply_canonical_involution
from discrepancy import compute_discrepancy

TOL = 1e-8

def check_involution_condition(system, order_k=1):
    """
    Pipeline completo de verificación de involución:
    1. Prolongar el sistema
    2. Aplicar involución canónica
    3. Calcular discrepancia
    """
    prolonged = prolong(system, order_k)
    involuted = apply_canonical_involution(prolonged, order_k)
    discrepancy = compute_discrepancy(prolonged, involuted)

    # Si todas las discrepancias son menores que TOL, está en involución
    if all(abs(val) < TOL for val in discrepancy.values()):
        return True, discrepancy

    return False, discrepancy


if __name__ == "__main__":
    print("Running involution check...")

    # Ejemplo numérico compatible
    example_system = {
        "u_x": 1.0,
        "u_y": 2.0
    }

    print(check_involution_condition(example_system, 1))
