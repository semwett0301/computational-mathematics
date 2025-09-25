## Computational Mathematics — Lab 5

### Task
Interpolate a function using tabulated data (nodes) or a known analytic function sampled on [a, b] with a given step. For a user-specified argument x, compute approximate values by several interpolation formulas and compare results.

Implemented methods:
- Lagrange interpolation polynomial (arbitrary nodes)
- Gauss central-difference formula (requires equally spaced nodes)
- Stirling formula (central, requires odd number of equally spaced nodes)
- Bessel formula (semi-central, requires even number of equally spaced nodes)

### Project structure
- `main.py`: selects input source, collects nodes, asks for argument x, runs all methods, prints results and draws plots
- `io_part/input.py`: interactive prompts; reads nodes from keyboard or `input.txt`; supports sampling of a built-in function
- `io_part/output.py`: prints each method’s value or states if the method is inapplicable
- `io_part/drawing.py`: plots the sampled function (if chosen) together with the nodes
- `math_part/interpolate_methods.py`: implementations of Lagrange, Gauss, Stirling, Bessel; spacing and parity checks
- `math_part/functions.py`: library of example functions and utility to sample nodes
- `input.txt`: example nodes file

### Requirements
- Python 3.9+
- Package: `termcolor`

Install (recommended in a virtual environment):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install termcolor
```

### How to run
From this directory:
```bash
python3 main.py
```

You will be prompted to:
- Choose input source: provide nodes or sample a built-in function
- If nodes: choose file or keyboard input
- If function: choose function, interval [a, b], and step
- Enter the argument x where interpolation is required

### File formats
Input file `input.txt` example:
```
X Y
0.5 1.532
0.55 2.5356
0.6 3.5406
0.65 4.5462
0.7 5.5504
0.75 6.5559
0.8 7.5594
```

### Method applicability
- Gauss/Stirling/Bessel require uniform spacing h. The code verifies uniformity; if violated, the method is reported as inapplicable.
- Stirling requires an odd number of nodes; Bessel requires an even number. The program checks and reports when conditions are not met.


