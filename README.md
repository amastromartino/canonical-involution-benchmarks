# Canonical Involution Benchmarks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package implementing the α_θ^(k) method for canonical involution verification with reproducible benchmark results.

## 📋 Features

- Implementation of the α_θ^(k) method for efficient integrability verification
- Comparison with traditional Cartan-Kähler approach
- Benchmark scripts to reproduce Table 2 from the paper
- Example systems for testing (involutive and non-involutive)
- Integration with SymPy for symbolic computation

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/amastromartino/canonical-involution-benchmarks.git
cd canonical-involution-benchmarks

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run basic examples
python examples/involutive_example.py
python examples/non_involutive_example.py

# 4. Reproduce benchmark results (Table 2 from paper)
python benchmarks/generate_table2.py
