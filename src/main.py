from prolongation import prolong
from involution import apply_canonical_involution
from discrepancy import compute_discrepancy

TOL = 1e-8

def check_involution_condition(system, order_k):
    prolonged = prolong(system, order=1)
    involuted = apply_canonical_involution(prolonged, order_k)
    discrepancy = compute_discrepancy(prolonged, involuted)

    if discrepancy < TOL:
        return True, []
    return False, ["Missing integrability conditions"]

if __name__ == "__main__":
    print("Running involution check...")
    example_system = {"u_x": 1.0, "u_y": 2.0}
    print(check_involution_condition(example_system, 1))
