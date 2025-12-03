Canonical Involution Benchmarks
A Python package implementing the alpha-theta method for canonical involution verification with reproducible benchmark results.

Features
Implementation of the alpha-theta method for efficient integrability verification

Comparison with traditional Cartan-Kähler approach

Benchmark scripts to reproduce Table 2 from the paper

Example systems for testing (involutive and non-involutive)

Integration with SymPy for symbolic computation

Quick Start
Clone the repository
git clone https://github.com/amastromartino/canonical-involution-benchmarks.git
cd canonical-involution-benchmarks
Install dependencies
pip install -r requirements.txt
Run basic examples
python examples/involutive_example.py
python examples/non_involutive_example.py
Reproduce benchmark results (Table 2 from paper)
python benchmarks/generate_table2.py
Benchmark Results
To reproduce Table 2 from our paper:
python benchmarks/generate_table2.py
Output:
================================================================================
BENCHMARK RESULTS - alpha-theta vs Cartan-Kähler Method
================================================================================
(n,m,k)    alpha-theta Ops  C-K Ops    Reduction    Accuracy
--------------------------------------------------------------------------------
(2,1,2)          45        180        4.0x        100%
(3,2,2)         120       1500       12.5x        100%
(4,3,2)         380      12000       31.6x        100%
(3,2,3)         850      45000       52.9x        100%
(4,3,3)        3200     280000       87.5x        100%
================================================================================
Project Structure
canonical-involution-benchmarks/
├── benchmarks/          # Benchmark scripts
├── examples/           # Example systems
├── figures/           # Generated figures
├── notebooks/         # Jupyter notebooks
├── src/              # Source code
├── README.md         # This file
├── requirements.txt  # Dependencies
└── setup.py         # Package configuration
Basic Usage
from src.main import check_involution_condition
import sympy as sp

x = sp.Symbol("x")
y = sp.Function("y")(x)
p = sp.diff(y, x)

system = {
    "eq1": sp.Eq(p, x**2),
    "eq2": sp.Eq(sp.Symbol('u'), p**2)
}

result = check_involution_condition(system, x, y)
print(f"Is involutive: {result['is_involutive']}")
License
MIT License



