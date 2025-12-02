# main.py

from prolongation import prolong
from involution import apply_canonical_involution
from discrepancy import compute_discrepancy

TOL = 1e-8


def check_involution_condition(system, order_k=1):
    """
    Aplica la cadena:
        1. Prolongación simbólica
        2. Involución canónica simplificada
        3. Discrepancia simbólica entre sistemas

    Si la discrepancia es cero → sistema en involución.
    """
    prolonged = prolong(system, order=order_k)
    involuted = apply_canonical_involution(prolonged, order_k)
    discrepancy = compute_discrepancy(prolonged, involuted)

    # Si todas las discrepancias son 0 → OK
    if all(val == 0 for val in discrepancy.values()):
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
