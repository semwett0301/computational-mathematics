## Computational Mathematics — Lab 1

### Task
Solve a system of linear algebraic equations (SLAE) AX = B. Implement a direct method that:
- Computes the triangular form (Gaussian elimination)
- Outputs the transformed (upper-triangular) matrix including the transformed right-hand side b
- Outputs the vector of unknowns x
- Outputs the residuals vector r = Ax − b

Input must be available from keyboard or from a file. Matrix size k ≤ 20.

This implementation focuses on the direct method (Gaussian elimination with back substitution). The determinant of the triangular matrix is used to check applicability (if det = 0 → method is not applicable).

### Project structure
- `main.py`: entry point; reads input, runs the method, prints results
- `input_output.py`: high-level I/O (choosing keyboard/file, pretty printing)
- `input_output_instruments.py`: low-level input helpers and validation
- `matrix_instruments.py`: Gaussian elimination and determinant/back-substitution helpers
- `matrix_interaction.py`: orchestration of elimination and residuals computation
- `index`: example input file

### Requirements
- Python 3.9+
- Package: `termcolor`

Install in a virtual environment (recommended):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install termcolor
```

### How to run
From this directory:
```bash
python3 main.py
```

You will be prompted:
- `Хотите ли вы ввести данные из файла? (y/n)`
  - Enter `n` to type the matrix and b column from keyboard
  - Enter `y` to read from a file (see format below)

If you choose file input, provide a path relative to the current directory when prompted. An example file `index` is included.

### Input format (file)
First line: integer k — matrix size (k ≤ 20)
Next k lines: coefficients of a row of A, then a separator `|`, then the corresponding right-hand side value bᵢ.

Example (`index`):
```
3
23 5 3 | 4
2 3 4 | 2
5 3 1 | 1
```

### Output
If the determinant of the triangular matrix is non-zero, the program prints:
- Transformed matrix (upper-triangular after forward elimination)
- Vector of unknowns x
- Residuals vector r = Ax − b

If the determinant equals zero, an error is printed: the method is not applicable.
