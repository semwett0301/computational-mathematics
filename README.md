# Computational Mathematics and Probability Theory Assignments

This repository contains coursework solutions and small programs for university labs in computational mathematics and a practical assignment in probability theory. There is no general-purpose app here — only task-focused scripts and utilities for the listed subjects.

## Repository structure
- `lab_1_math/`: Solve a linear system Ax = b with Gaussian elimination; print transformed matrix, solution, and residuals. Interactive/file input supported.
- `lab2_math/`: Nonlinear equations and systems. Methods: Chord (secant), Simple iterations, and Newton (for systems). Includes plotting and file/console I/O.
- `lab3_math/`: Numerical integration. Rectangle (left/right/middle) and trapezoid rules. Handles proper and some improper integrals with convergence checks.
- `lab4_math/`: Least-squares approximation of tabular data. Models: linear, quadratic, cubic, logarithmic, exponential, power; selects best by minimal σ and plots.
- `lab5_math/`: Interpolation. Lagrange, Gauss, Stirling, and Bessel formulas over user-provided or sampled nodes. Prints values and draws graphs.
- `lab6_math/`: Initial value problems for first-order ODEs. Explicit Euler (with adaptive control) and Milne predictor–corrector; tables and plots vs exact solution.
- `theory_of_possibility_5/`: Probability theory practical 5 — descriptive stats for a small sample, EDF, histogram/density, and frequency polygon.

Each subfolder has its own `README.md` with details, dependencies, and usage instructions.

## Requirements
- Python 3.9+ (tested locally)
- Depending on the lab: `numpy`, `sympy`, `matplotlib`, `seaborn`, `pandas`, `termcolor`

It’s recommended to create a virtual environment per lab and install only the packages listed in that lab’s README.

## How to run
Navigate into a specific lab directory and run its main script, for example:
```bash
cd lab3_math
python3 main.py
```
Interactive prompts (in Russian) will guide input. Some labs support reading from simple text files in the same directory and plotting results.


