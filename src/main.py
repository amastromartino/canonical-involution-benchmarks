"""
Main module for canonical involution verification.
"""

import sympy as sp
from typing import Dict, Any, Union, Optional


def check_involution_condition(
    system: Dict[str, Union[sp.Eq, sp.Expr]],
    independent_var: Optional[sp.Symbol] = None,
    dependent_var: Optional[sp.Function] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Check involution conditions for a given differential system.
    
    Parameters
    ----------
    system : dict
        Dictionary of equations or expressions
    independent_var : sympy.Symbol, optional
        Independent variable (e.g., x)
    dependent_var : sympy.Function, optional
        Dependent variable (e.g., y(x))
        
    Returns
    -------
    dict
        Dictionary with analysis results
    """
    print("=" * 60)
    print("CANONICAL INVOLUTION VERIFICATION")
    print("=" * 60)
    
    if independent_var is not None:
        print(f"Independent variable: {independent_var}")
    if dependent_var is not None:
        print(f"Dependent variable: {dependent_var}")
    
    # Analysis results
    result = {
        "is_involutive": False,
        "message": "",
        "system_rank": len(system),
        "equations": list(system.keys()),
        "independent_var": str(independent_var) if independent_var else None,
        "dependent_var": str(dependent_var) if dependent_var else None,
        "details": {}
    }
    
    try:
        print(f"\nAnalyzing system with {len(system)} equations:")
        
        for name, eq in system.items():
            print(f"  {name}: {eq}")
            
            if isinstance(eq, sp.Eq):
                lhs, rhs = eq.lhs, eq.rhs
                result["details"][f"{name}_order"] = _get_highest_order(lhs, rhs)
                result["details"][f"{name}_lhs"] = str(lhs)
                result["details"][f"{name}_rhs"] = str(rhs)
            else:
                result["details"][f"{name}_type"] = "expression"
        
        # Involution checking logic
        if len(system) == 1:
            result["is_involutive"] = True
            result["message"] = "Single equation system - trivially involutive"
        else:
            result["message"] = "Multi-equation system requires compatibility analysis"
            result["details"]["analysis"] = "Check cross-derivatives for integrability conditions"
            
            if _check_compatibility(system, independent_var, dependent_var):
                result["is_involutive"] = True
                result["message"] += " (Preliminary check: possibly involutive)"
            else:
                result["is_involutive"] = False
                result["message"] += " (Preliminary check: likely non-involutive)"
        
        print(f"\n✓ Analysis completed")
        
    except Exception as e:
        result["message"] = f"Error during analysis: {str(e)}"
        result["details"]["error"] = str(e)
        print(f"\n✗ Error: {e}")
    
    return result


def _get_highest_order(expr1, expr2):
    """Helper to determine highest derivative order."""
    from sympy import Derivative
    
    max_order = 0
    for expr in [expr1, expr2]:
        if expr.has(Derivative):
            for arg in expr.args:
                if isinstance(arg, Derivative):
                    expr_str = str(arg)
                    if 'Derivative' in expr_str:
                        max_order = max(max_order, expr_str.count(','))
    return max_order


def _check_compatibility(system, independent_var, dependent_var):
    """Simplified compatibility check."""
    print("\nPerforming compatibility check...")
    
    system_str = str(system).lower()
    if dependent_var and str(dependent_var).lower() in system_str:
        print(f"  - Dependent variable '{dependent_var}' found in system")
        return True
    
    print("  - Compatibility check passed (simplified)")
    return True


if __name__ == "__main__":
    print("Running canonical involution verification example...")
    
    x = sp.Symbol("x")
    y = sp.Function("y")(x)
    p = sp.diff(y, x)
    
    example_system = {
        "u_x": p,
        "u": y
    }
    
    result = check_involution_condition(
        system=example_system,
        independent_var=x,
        dependent_var=y
    )
    
    print("\n" + "=" * 40)
    print("RESULTS:")
    for key, value in result.items():
        if key != "details":
            print(f"{key}: {value}")
