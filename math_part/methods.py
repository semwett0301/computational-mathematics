import sympy as sp
from math_part import own_functions as own


def integrate_non_break_function(function, method_number, a, b, accuracy):
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

    return second_value, n * 2


def integrate_break_function(function_number, method_number, a, b, accuracy):
    if function_number == 2 and b > 2:
        return None, None

    x = sp.symbols('x')
    c = sp.symbols('c')
    if a in own.functions_with_break[function_number]["break"]:
        if function_number == 1:
            lim = sp.limit(sp.integrate(1 / x ** 3, (x, c, b)), c, a, "+")
        elif function_number == 2:
            lim = sp.limit(sp.integrate(1 / (2 - x) ** 0.5, (x, c, b)), c, a, "+")
        else:
            lim = sp.limit(sp.integrate(sp.sin(x) / x, (x, c, b)), c, a, "+")
        if lim == -sp.oo or lim == sp.oo or lim is None:
            return None, None
        return integrate_non_break_function(own.functions_with_break[function_number]["value"], method_number,
                                            a + 0.00000001, b, accuracy)

    elif b in own.functions_with_break[function_number]["break"]:
        if function_number == 1:
            lim = sp.limit(sp.integrate(1 / x ** 3, (x, a, c)), c, b, "-")
        elif function_number == 2:
            lim = sp.limit(sp.integrate(1 / (2 - x) ** 0.5, (x, a, c)), c, b, "-")
        else:
            lim = sp.limit(sp.integrate(sp.sin(x) / x, (x, a, c)), c, b, "-")
        if lim == -sp.oo or lim == sp.oo or lim is None:
            return None, None
        return integrate_non_break_function(own.functions_with_break[function_number]["value"], method_number, a,
                                            b - 0.00000001, accuracy)

    brr = None
    for i in own.functions_with_break[function_number]["break"]:
        if a < i < b:
            brr = i
    if brr is None:
        return integrate_non_break_function(own.functions_with_break[function_number]["value"], method_number, a, b,
                                            accuracy)
    else:
        if function_number == 1:
            lim_1 = sp.limit(sp.integrate(1 / x ** 3, (x, a, c)), c, brr, "+")
            lim_2 = sp.limit(sp.integrate(1 / x ** 3, (x, c, b)), c, brr, "-")
        elif function_number == 2:
            lim_1 = sp.limit(sp.integrate(1 / (2 - x) ** 0.5, (x, a, c)), c, brr, "+")
            lim_2 = sp.limit(sp.integrate(1 / (2 - x) ** 0.5, (x, c, b)), c, brr, "-")
        else:
            lim_1 = sp.limit(sp.integrate(sp.sin(x) / x, (x, a, c)), c, brr, "+")
            lim_2 = sp.limit(sp.integrate(sp.sin(x) / x, (x, c, b)), c, brr, "-")
        if lim_1 == -sp.oo or lim_1 == sp.oo or lim_1 is None or lim_2 == -sp.oo or lim_2 == sp.oo or lim_2 is None:
            return None, None

        int_1, n_1 = integrate_non_break_function(own.functions_with_break[function_number]["value"], method_number, a,
                                                  brr - 0.00000001, accuracy)
        int_2, n_2 = integrate_non_break_function(own.functions_with_break[function_number]["value"], method_number,
                                                  brr + 0.00000001, b, accuracy)

        return float(int_1) + float(int_2), n_1 + n_2
