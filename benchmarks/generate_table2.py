#!/usr/bin/env python
"""
Script to generate Table 2 from the paper.
Run with: python generate_table2.py
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from alpha_theta_method import generate_benchmark_table

def main():
    """Generate and display the benchmark table."""
    print("\n" + "="*80)
    print("REPRODUCING TABLE 2: Experimental operations for integrability verification")
    print("="*80)
    
    results = generate_benchmark_table()
    
    # Save to CSV
    import csv
    with open('benchmark_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'm', 'k', 'alpha_theta_ops', 'cartan_kahler_ops', 'reduction', 'accuracy'])
        for r in results:
            n, m, k = r['config']
            writer.writerow([n, m, k, r['alpha_theta_ops'], r['cartan_kahler_ops'], 
                           r['reduction'], r['accuracy']])
    
    print(f"\nResults saved to 'benchmark_results.csv'")
    print("\nTo cite these results in your paper:")
    print("The benchmark data was generated using the α_θ^(k) implementation")
    print("available at: https://github.com/amastromartino/canonical-involution-benchmarks")

if __name__ == "__main__":
    main()
