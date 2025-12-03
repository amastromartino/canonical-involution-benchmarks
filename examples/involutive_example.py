"""
Involutive system example for comparison.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.main import check_involution_condition
except ImportError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
    from main import check_involution_condition

import sympy as sp


def main():
    """Run involutive example."""
    x = sp.Symbol("x")
    y = sp.Function("y")(x)
    p = sp.diff(y, x)
    
    # Simple involutive system
    system = {
        "trivial_eq": sp.Eq(p, 0),  # y' = 0
    }
    
    print("=" * 60)
    print("INVOLUTIVE SYSTEM EXAMPLE")
    print("=" * 60)
    print("System: y' = 0")
    print("\nThis is a trivially involutive system.")
    print("=" * 60)
    
    # Now call with correct number of arguments
    result = check_involution_condition(
        system=system,
        independent_var=x,
        dependent_var=y
    )
    
    # Display results
    print("\n" + "=" * 60)
    print("VERIFICATION RESULTS")
    print("=" * 60)
    
    print(f"\nSystem analyzed: {len(system)} equation(s)")
    print(f"Is involutive: {result.get('is_involutive', False)}")
    print(f"Message: {result.get('message', 'No message')}")
    
    if 'details' in result:
        print("\nDetailed analysis:")
        for key, value in result['details'].items():
            if 'expr' in key or 'lhs' in key or 'rhs' in key:
                print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("Expected: This system should be INVOLUTIVE")
    print("Reason: Single first-order equation")
    print("=" * 60)
    
    return result


if __name__ == "__main__":
    main()
