import math

import numpy as np

functions = {
    1: {
        "function": "y' = x^3 - y на [0; 2] при y(0) = 0",
        "value": lambda x, y: x ** 3 - y,
        "solution": lambda x: x ** 3 - 3 * x ** 2 + 6 * x + 6 * np.exp(-x) - 6,
        "a": 0,
        "b": 2,
        "y0": 0
    },
    2: {
        "function": "y' = y + (1 + x) * y^2 на [1; 1.5] при y(1) = -1",
        "value": lambda x, y: y + (1 + x) * y ** 2,
        "solution": lambda x: - 1 / x,
        "a": 1,
        "b": 1.5,
        "y0": -1
    },
    3: {
        "function": "y' = x + 1 - y на [1; 1.6] при y(1) = 2",
        "value": lambda x, y: x + 1 - y,
        "solution": lambda x: np.exp(1 - x) + x,
        "a": 1,
        "b": 1.6,
        "y0": 2
    }
}