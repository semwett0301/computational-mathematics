import math

import numpy as np

functions = {
    1: {
        "function": "y' = y - 2 * (2 + x) * y^3 на [1; 2] при y(1) = -5",
        "value": lambda x, y: y - 2 * (2 + x) * y ** 3,
        "solution": lambda x: x,
        "a": 1,
        "b": 2,
        "y0": -5
    },
    2: {
        "function": "y' = y + (1 + x) * y^2 на [1; 1.5] при y(1) = -1",
        "value": lambda x, y: y + (1 + x) * y ** 2,
        "solution": lambda x: - 1 / x,
        "a": 1,
        "b": 1.5,
        "y0": -1
    }
}