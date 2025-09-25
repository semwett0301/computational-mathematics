import numpy as np
import sympy as sp

single_functions = {
    1: {
        "function": "x^3 - x + 4",
        "value": lambda x: x ** 3 - x + 4
    },
    2: {
        "function": "x^3 - 3,125x^2 - 3,5x + 2,458",
        "value": lambda x: x ** 3 - x ** 2 * 3.125 - 3.5 * x + 2.458
    },
    3: {
        "function": "2,3x^3 + 5,75x^2 - 7,41x - 10,6",
        "value": lambda x: 2.3 * x ** 3 + 5.75 * x ** 2 - 7.41 * x - 10.6
    },
    4: {
        "function": "sin(x)^2 + cos(x)",
        "value": lambda x: np.sin(x) ** 2 + np.cos(x)
    }
}

system_functions = {
    1: {
        "function": "x^2 + y^2 - 4",
        "value": lambda x, y: x ** 2 + y ** 2 - 4
    },
    2: {
        "function": "y - 3x^2",
        "value": lambda x, y: y - 3 * x ** 2
    },
    3: {
        "function": "3x^3 -2x + 1 - y",
        "value": lambda x, y: 3 * x ** 3 - 2 * x + 1 - y
    },
    4: {
        "function": "cos(x)^3 + sin(x) - sin(y)",
        "value": lambda x, y: sp.cos(x) ** 3 + sp.sin(x) - sp.sin(y)
    }
}
