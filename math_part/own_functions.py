import numpy as np

functions = {
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