from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="canonical-involution-benchmarks",
    version="0.1.0",
    author="Ángel Mastromartino",
    author_email="tuemail@example.com",
    description="Benchmarks for canonical involution verification in differential systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/canonical-involution-benchmarks",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sympy>=1.12",
    ],
)
