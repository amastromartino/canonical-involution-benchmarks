
# Canonical Involution Benchmarks  
Verificación computacional de la involución canónica y condiciones de integrabilidad en sistemas diferenciales de orden superior.

Este repositorio contiene una implementación mínima, reproducible y extensible del pipeline descrito en el artículo **“Invariants, Solutions and Involution of Higher Order Differential Systems” (Mastromartino, 2020)**, con el objetivo de evaluar:

- La **involución canónica** en espacios de jets.
- La **consistencia de derivadas mezcladas**.
- La **integrabilidad formal** de sistemas diferenciales.
- La reproducción de ejemplos numéricos y simbólicos.

El código está organizado de manera modular para permitir ampliaciones posteriores hacia modelos reales y aplicaciones geométricas más avanzadas.

---

## 📁 Estructura del repositorio

canonical-involution-benchmarks/
│
├── src/
│ ├── main.py # Script principal del pipeline
│ ├── prolongation.py # Prolongación de un sistema (orden 1 por defecto)
│ ├── involution.py # Implementación simplificada de la involución canónica
│ └── discrepancy.py # Métrica de discrepancia entre sistemas
│
├── examples/ # (Opcional) Ejemplos numéricos y simbólicos
│
├── notebooks/ # Notebooks demostrativos
│
├── benchmarks/ # Scripts de prueba y tiempos
│
├── figures/ # Ilustraciones (si se requieren)
│
├── LICENSE # Licencia MIT
└── README.md # Este archivo
