def calculate_det(function):
    h = 0.000000001
    return lambda x: (function(x + h) - function(x - h)) / (2 * h)


def calculate_second_det(function):
    h = 0.000000001
    return lambda x: (calculate_det(function)(x + h) - calculate_det(function)(x - h)) / (2 * h)


def get_max_det_value(function, a, b):
    if calculate_det(function)(a) > calculate_det(function)(b):
        return abs(calculate_det(function)(a))
    else:
        return abs(calculate_det(function)(b))


# Для системы

def calculate_det_x(function, x, y):
    h = 0.00000001
    return (function(x + h, y) - function(x - h, y)) / (2 * h)


def calculate_det_y(function, x, y):
    h = 0.00000001
    return (function(x, y + h) - function(x, y - h)) / (2 * h)


def calculate_jackobian(f_func, g_func, x, y):
    return calculate_det_x(f_func, x, y) * calculate_det_y(g_func, x, y) - calculate_det_x(g_func, x, y) * calculate_det_y(f_func, x, y)
