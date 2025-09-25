# Computational Mathematics — Lab 3

## Task
Compute definite integrals of user-chosen functions on [a, b]. Support functions without discontinuities and improper integrals (with first-kind breaks at an endpoint or inside the interval). Provide the integral value and, for proper integrals, the number of subintervals needed to achieve the requested accuracy.

Implemented numerical methods:
- Rectangles: left, right, middle
- Trapezoid rule

For improper integrals the program checks convergence using symbolic limits and only computes the value if the integral converges.

## Project structure
- `main.py`: entry point; reads parameters, selects function/method/mode, runs integration, prints results
- `io_part/input.py`: interactive input (mode, function, method, bounds, accuracy)
- `io_part/output.py`: formatted output
- `math_part/methods.py`: composite rules with Runge error control; convergence checks and splitting at breaks
- `math_part/own_functions.py`: catalogs of functions with and without breaks

## Requirements
- Python 3.9+
- Packages: `numpy`, `sympy`, `termcolor`

Install (recommended in a virtual environment):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy sympy termcolor
```

### How to run
From this folder:
```bash
python3 main.py
```

Interactive prompts (in Russian):
- Choose mode: integrate a function without a break or with a break
- Choose the function from the provided list
- Choose the method: left/right/middle rectangles, trapezoid
- Enter integration bounds a and b (order doesn’t matter) and accuracy e (> 0)

## Output
- For functions without breaks: prints the integral value and the minimal number of subintervals `n` needed to meet the accuracy (Runge criterion with k = 2)
- For functions with breaks: if the improper integral converges, prints the integral value; if it diverges or is undefined, prints an error