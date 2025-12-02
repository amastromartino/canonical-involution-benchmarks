Canonical Involution Benchmarks

Verificación computacional de la involución canónica y condiciones de integrabilidad en sistemas diferenciales de orden superior.

Este repositorio contiene una implementación mínima, reproducible y extensible del pipeline descrito en el artículo “Invariants, Solutions and Involution of Higher Order Differential Systems” (Mastromartino, 2020), con el objetivo de evaluar:

La involución canónica en espacios de jets.

La consistencia de derivadas mezcladas.

La integrabilidad formal de sistemas diferenciales.

La reproducción de ejemplos numéricos y simbólicos.

El código está organizado de manera modular para permitir ampliaciones posteriores hacia modelos reales y aplicaciones geométricas más avanzadas.
📁 Estructura del repositorio
canonical-involution-benchmarks/
│
├── src/
│   ├── main.py                     # Script principal del pipeline
│   ├── prolongation.py             # Prolongación de un sistema
│   ├── involution.py               # Implementación simplificada de la involución
│   └── discrepancy.py              # Métrica de discrepancia entre sistemas
│
├── examples/                       # (Opcional) Ejemplos numéricos y simbólicos
├── notebooks/                      # Notebooks demostrativos
├── benchmarks/                     # Scripts de prueba y tiempos
├── figures/                        # Ilustraciones
│
├── LICENSE                         # Licencia MIT
└── README.md                       # Este archivo

Ejecución rápida
1. Clonar el repositorio
2. git clone https://github.com/amastromartino/canonical-involution-benchmarks
cd canonical-involution-benchmarks
pip install -r requirements.txt
2. Ejecutar el pipeline
cd src
python main.py
Salida esperada:
Running involution check...
(True, [])
nterpretación:

True → el sistema cumple involución en su forma actual.

[] → no se detectaron fallas de integrabilidad.
¿Qué es la involución canónica?

La involución canónica es una transformación geométrica en espacios de jets que:

Reordena derivadas mezcladas.

Garantiza la consistencia formal del sistema.

Identifica fallas de integrabilidad antes de resolver un sistema.

Se relaciona con:

propiedad de submersión,

clausura de ideales diferenciales,

existencia de soluciones regulares.

La implementación completa requiere:

la distribución de Cartan,

derivadas iteradas,

estructura del fibrado de jets.

Aquí se incluye una versión educativa, verificable y simplificada.

📊 Notebooks incluidos

(Se habilitarán próximamente)

Ejemplo numérico simple

Ejemplo simbólico con SymPy

Comparación de discrepancias bajo prolongación

Evaluación de estabilidad de la involución

📚 Referencias

A. Mastromartino, Invariants, Solutions and Involution of Higher Order Differential Systems, Matematički Vesnik, 2020.

P. Olver, Applications of Lie Groups to Differential Equations, Springer.

D. Sauzin, Introduction to Jet Bundles, Lecture Notes.

📝 Licencia

Este proyecto está disponible bajo la Licencia MIT, permitiendo uso académico y comercial con atribución.

🤝 Contribuciones

Las contribuciones son bienvenidas:

Nuevos ejemplos

Implementaciones para jets de orden superior

Benchmarks

Visualizaciones geométricas

Abre un Issue o un Pull Request.

🔍 Estado actual del proyecto

Versión simplificada y funcional del pipeline geométrico.
Base para:

Documentación académica

Benchmarks reproducibles

Implementaciones futuras más profundas

