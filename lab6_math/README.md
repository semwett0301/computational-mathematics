## Computational Mathematics — Lab 6

### Task
Numerically solve initial value problems for first-order ODEs on [a, b] with step h and target accuracy e. Build a table of approximate values and estimate accuracy using Runge-type control. Visualize the numerical solutions against the exact solution.

Implemented methods:
- Explicit Euler method with adaptive halving until local Runge estimate ≤ e
- Milne predictor–corrector method with iterative correction to tolerance e

### Project structure
- `main.py`: selects an ODE from a built-in set, reads h and e, runs all methods, prints tables, and plots
- `io_part/input.py`: prompts for function choice and positive parameters h, e
- `io_part/output.py`: tabulates (x, y_method, y_exact, |error|) per method
- `io_part/drawing.py`: plots numerical solutions and the exact solution on the same axes
- `math_part/functions.py`: predefined ODEs f(x, y), exact solutions y(x), intervals [a, b], and y(a)
- `math_part/methods.py`: implementations of Euler and Milne methods

### Requirements
- Python 3.9+
- Packages: `numpy`, `matplotlib`, `termcolor`

Install (recommended in a virtual environment):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy matplotlib termcolor
```

### How to run
From this directory:
```bash
python3 main.py
```

You will be prompted to choose an ODE (with defined [a, b] and y(a)), then to enter step `h` and accuracy `e`. The program computes points for both methods, prints tables with exact values and absolute errors, and opens a plot comparing methods to the exact solution.

