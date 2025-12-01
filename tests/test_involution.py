from src.main import check_involution_condition

def test_involution_basic():
    system = {"u_x": 1.0, "u_y": 2.0}
    ok, missing = check_involution_condition(system, 2)

    assert isinstance(ok, bool)
    assert isinstance(missing, list)
