"""
Non-involutive system example for canonical involution verification.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now imports work both for runtime and for reviewers
try:
    from src.main import check_involution_condition
except ImportError:
    # Alternative import for direct execution
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
    from main import check_involution_condition

import sympy as sp


def main():
    """Run the non-involutive example."""
    
    # Define symbols
    x = sp.Symbol("x")
    y = sp.Function("y")(x)
    p = sp.diff(y, x)
    
    # Define the non-involutive system
    system = {
        "y_prime_eq": sp.Eq(p, x**2),           # y' = x^2
        "u_eq": sp.Eq(sp.Symbol('u'), p**2)     # u = (y')^2
    }
    
    print("=" * 70)
    print("NON-INVOLUTIVE SYSTEM EXAMPLE")
    print("=" * 70)
    print("System:")
    print("  1. y' = x^2")
    print("  2. u = (y')^2")
    print("\nThis system is incompatible and non-holonomic.")
    print("=" * 70)
    
    # Check involution condition
    result = check_involution_condition(
        system=system,
        independent_var=x,
        dependent_var=y
    )
    
    # Display results
    print("\n" + "=" * 70)
    print("VERIFICATION RESULTS")
    print("=" * 70)
    
    print(f"\nSystem analyzed: {len(system)} equations")
    print(f"Is involutive: {result.get('is_involutive', False)}")
    print(f"Message: {result.get('message', 'No message')}")
    
    if 'details' in result:
        print("\nDetailed analysis:")
        for key, value in result['details'].items():
            if key.endswith('_order') or 'analysis' in key:
                print(f"  {key}: {value}")
    
    print("\n" + "=" * 70)
    print("Expected: This system should be NON-INVOLUTIVE")
    print("Reason: The equations are incompatible")
    print("=" * 70)
    
    return result


if __name__ == "__main__":
    main()
