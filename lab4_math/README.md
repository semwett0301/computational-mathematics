# Computational Mathematics — Lab 4

## Task
Given a set of experimental points (xᵢ, yᵢ), build empirical models by least squares, compute the total squared error S and root-mean-square deviation σ for each model, choose the best approximation (smallest σ), and plot data with the fitted curves.

Implemented approximations:
- Linear
- Quadratic
- Cubic
- Logarithmic (requires x > 0)
- Exponential (requires y > 0)
- Power (requires x > 0 and y > 0)

For the linear model, the Pearson correlation coefficient r is also computed.

## Project structure
- `main.py`: input selection, runs all approximations, selects best σ, outputs results, plots
- `io_part/input.py`: read points from keyboard or `input.txt`
- `io_part/output.py`: print/save results and draw plots
- `math_part/approximate_functions.py`: least-squares formulas and normal-equations solving
- `math_part/matrix_interaction.py`: Gaussian elimination with partial pivoting for normal systems
- `input.txt`: example data file

## Requirements
- Python 3.9+
- Packages: `numpy`, `matplotlib`, `termcolor`

Install (recommended in a virtual environment):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy matplotlib termcolor
```

## How to run
From this directory:
```bash
python3 main.py
```

You will be asked:
- Input source: file or keyboard
- If keyboard: number of points and then each `x y` pair
- Output destination: screen or file

## File formats
- Input file `input.txt` example:
```
X Y
1.1 3.5
2.3 4.1
-3.7 5.2
4.5 6.9
5.4 8.3
6.8 14.8
7.5 21.2
```
- Output: when saving to file, results are written to `output.txt` with, for each model, the formula, S, σ, possibly r (linear), plus the best model summary.

## Method details
- Each model uses closed-form least-squares normal equations to compute parameters; where applicable, inputs are transformed (log/exp) before linearization.
- If the normal-equation determinant is zero or domain constraints are violated, that model is skipped and reported as not computed.
- σ is computed as sqrt(S / n). The model with the minimal σ is reported as best.


