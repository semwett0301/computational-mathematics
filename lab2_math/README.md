## Computational Mathematics — Lab 2

### Task
Solve a nonlinear equation f(x) = 0 on [a, b] or a system of two nonlinear equations F(x, y) = 0. Implement iterative numerical methods with convergence checks and provide both console and file I/O.

- For a single equation: Chord (secant) method and Simple iterations method
- For a system (2 equations): Newton's method
- Visualize: plot f(x) for single equation and implicit plots for systems

### Project structure
- `main.py`: program entry; reads inputs, selects mode/method, runs solver, outputs results and plots
- `io_part/input.py`: user interaction and reading from files `input_single.txt` or `input_system.txt`
- `io_part/output.py`: printing to console or writing to `output.txt`
- `io_part/drawing.py`: plots for single functions and systems
- `math_part/methods.py`: implementations of methods (Chord, Simple iterations, Newton)
- `math_part/validation.py`: method-specific convergence and correctness checks
- `math_part/utils.py`: numerical derivatives and Jacobian helpers
- `math_part/own_functions.py`: predefined single functions and system functions
- `input_single.txt`, `input_system.txt`: example input files
- `output.txt`: example output file

### Requirements
- Python 3.9+
- Packages: `numpy`, `sympy`, `matplotlib`, `termcolor`

Install (in a virtual environment is recommended):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy sympy matplotlib termcolor
```

### How to run
From this directory:
```bash
python3 main.py
```

Interactive prompts (in Russian) will guide you:
- Choose: solve a single equation or a system
- For a single equation: choose a function and method (Chord or Simple iterations), then set [a, b] and error `e`
- For a system: choose two functions and initial guesses `(x0, y0)`, then set error `e`
- Choose whether to read parameters from files or keyboard, and whether to print to screen or save to file

### File input formats
If you choose to read from files, the program expects the following:

- `input_single.txt` (for single equation):
```
method=2
a=-2
b=-1
e=0.01
```
  - `method`: 1 → Chord, 2 → Simple iterations
  - `a`, `b`: interval endpoints (a < b)
  - `e`: required accuracy (> 0)

- `input_system.txt` (for system of two equations):
```
x=0.7
y=0.8
e=0.01
```
  - `x`, `y`: initial approximations `(x0, y0)`
  - `e`: required accuracy (> 0)

### Output
Depending on mode, results are printed to console or written to `output.txt`:
- Single equation: found root `x`, function value `f(x)` at the root, iteration count
- System: roots `x`, `y`, vector of final errors for each variable, iteration count

Additionally, the program opens plots:
- Single equation: graph of the chosen function over a default range
- System: implicit plots of both equations on the same axes

### Methods and validation
- **Chord (secant) method**: picks a fixed endpoint using the sign of f and f''; iterates until `|x_k − x_{k-1}| ≤ e` and `|f(x_k)| ≤ e`. Requires a sign change on [a, b] and additional monotonicity/convexity conditions.
- **Simple iterations**: constructs `φ(x) = x + λ f(x)`, automatically choosing `λ` from derivative bounds; uses contraction-based stopping with `q`. Validates `|φ'(x)| ≤ 1` at endpoints.
- **Newton for systems**: finite-difference Jacobian, updates `(x, y)` until both changes are within `e` or iteration cap is reached.


