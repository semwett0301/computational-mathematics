def integrate_function(function, method_number, a, b, accuracy):
    def left_rect(function, a, b, n):
        h = abs(b - a) / n
        integral = 0
        for i in range(n):
            integral += function(a + i * h) * h
        return integral

    def right_rect(function, a, b, n):
        h = abs(b - a) / n
        integral = 0
        for i in range(n):
            integral += function(a + (i + 1) * h) * h
        return integral

    def center_rect(function, a, b, n):
        h = abs(b - a) / n
        integral = 0
        for i in range(n):
            integral += function(a + i * h + h / 2) * h
        return integral

    def trapezoid(function, a, b, n):
        h = abs(b - a) / n
        integral = 0
        for i in range(n):
            integral += h / 2 * (function(a + i * h) + function(a + (i + 1) * h))
        return integral

    if method_number == 1:
        method = left_rect
        k = 2
    elif method_number == 2:
        method = right_rect
        k = 2
    elif method_number == 3:
        method = center_rect
        k = 2
    else:
        method = trapezoid
        k = 2

    n = 4
    first_value = method(function, a, b, n)
    second_value = method(function, a, b, n * 2)

    while abs((second_value - first_value) / (2 ** k - 1)) > accuracy:
        n *= 2
        first_value = method(function, a, b, n)
        second_value = method(function, a, b, n * 2)

    return first_value, n
