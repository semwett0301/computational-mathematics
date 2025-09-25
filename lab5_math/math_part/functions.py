import numpy as np

functions = {
    1: {
        "function": "sin(x)",
        "value": lambda x: np.sin(x)
    }
}


def get_points_from_function(function, a, b, step):
    points = []
    tmp_x = a
    while tmp_x <= b:
        points.append([tmp_x, function(tmp_x)])
        tmp_x += step
    return points
