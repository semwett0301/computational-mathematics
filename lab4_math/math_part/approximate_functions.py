import math
import numpy as np
from math_part import matrix_interaction as mi


def lin_app(points):
    s_x = 0
    s_x_x = 0
    s_y = 0
    s_x_y = 0
    for i in range(len(points)):
        s_x += points[i][0]
        s_x_x += points[i][0] ** 2
        s_y += points[i][1]
        s_x_y += points[i][0] * points[i][1]

    m_x = s_x / len(points)
    m_y = s_y / len(points)

    s_m_x_y = 0
    s_m_x = 0
    s_m_y = 0
    for i in range(len(points)):
        s_m_x_y += (points[i][0] - m_x) * (points[i][1] - m_y)
        s_m_x += (points[i][0] - m_x) ** 2
        s_m_y += (points[i][1] - m_y) ** 2

    # Коэффициент Пирсона
    try:
        r = round(s_m_x_y / math.sqrt(s_m_x * s_m_y), 3)
    except Exception:
        r = None

    n = len(points)
    delta = s_x_x * n - s_x ** 2
    delta_1 = s_x_y * n - s_x * s_y
    delta_2 = s_x_x * s_y - s_x * s_x_y

    try:
        a = round(delta_1 / delta, 3)
        b = round(delta_2 / delta, 3)
        result = lambda x: a * x + b
        result_func = str(a) + "x + " + str(b)

        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)
    except Exception:
        a = b = result_func = s = result = sigma = None

    return {
        "name": "Линейная",
        "function": result_func,
        "lambda": result,
        "s": s,
        "r": r,
        "sigma": sigma
    }


def squad_app(points):
    n = len(points)
    s_x = s_x_x = s_x_x_x = s_x_x_x_x = s_y = s_x_y = s_x_x_y = 0
    for i in range(len(points)):
        s_x += points[i][0]
        s_x_x += points[i][0] ** 2
        s_x_x_x += points[i][0] ** 3
        s_x_x_x_x += points[i][0] ** 4
        s_y += points[i][1]
        s_x_y += points[i][0] * points[i][1]
        s_x_x_y += points[i][0] * points[i][0] * points[i][1]

    matrix = [
        [n, s_x, s_x_x],
        [s_x, s_x_x, s_x_x_x],
        [s_x_x, s_x_x_x, s_x_x_x_x]
    ]

    results = [
        s_y,
        s_x_y,
        s_x_x_y
    ]

    a_0, a_1, a_2 = mi.calculating_unknowns(matrix, results)

    if a_0 == a_1 == a_2 == 0:
        function = s = sigma = result = None
    else:
        function = f"{round(a_2, 3)}x^2 + {round(a_1, 3)}x + {round(a_0, 3)}"
        result = lambda x: a_2 * x ** 2 + a_1 * x + a_0
        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)

    return {
        "name": "Квадратичная",
        "function": function,
        "lambda": result,
        "s": s,
        "sigma": sigma
    }


def qub_appr(points):
    n = len(points)
    s_x = s_x_2 = s_x_3 = s_x_4 = s_x_5 = s_x_6 = s_y = s_x_y = s_x_2_y = s_x_3_y = 0

    for i in range(len(points)):
        s_x += points[i][0]
        s_x_2 += points[i][0] ** 2
        s_x_3 += points[i][0] ** 3
        s_x_4 += points[i][0] ** 4
        s_x_5 += points[i][0] ** 5
        s_x_6 += points[i][0] ** 6

        s_y += points[i][1]
        s_x_y += points[i][0] * points[i][1]
        s_x_2_y += points[i][0] * points[i][0] * points[i][1]
        s_x_3_y += points[i][0] * points[i][0] * points[i][0] * points[i][1]

    matrix = [
        [n, s_x, s_x_2, s_x_3],
        [s_x, s_x_2, s_x_3, s_x_4],
        [s_x_2, s_x_3, s_x_4, s_x_5],
        [s_x_3, s_x_4, s_x_5, s_x_6]
    ]

    results = [
        s_y,
        s_x_y,
        s_x_2_y,
        s_x_3_y
    ]

    a_0, a_1, a_2, a_3 = mi.calculating_unknowns(matrix, results)

    if a_0 == a_1 == a_2 == a_3 == 0:
        function = s = sigma = result = None
    else:
        function = f"{round(a_3, 3)}x^3 + {round(a_2, 3)}x^2 + {round(a_1, 3)}x + {round(a_0, 3)}"
        result = lambda x: a_3 * x ** 3 + a_2 * x ** 2 + a_1 * x + a_0
        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)

    return {
        "name": "Кубическая",
        "function": function,
        "lambda": result,
        "s": s,
        "sigma": sigma
    }


def exp_appr(points):
    n = len(points)

    for i in points:
        if i[1] <= 0:
            return {
                "name": "Экспоненциальная",
                "function": None,
                "lambda": None,
                "s": None,
                "sigma": None
            }

    s_x = s_x_2 = s_y = s_x_y = 0
    for i in range(n):
        s_x += points[i][0]
        s_x_2 += points[i][0] ** 2
        s_y += math.log(points[i][1])
        s_x_y += math.log(points[i][1]) * points[i][0]

    delta = s_x_2 * n - s_x ** 2
    delta_1 = s_x_y * n - s_x * s_y
    delta_2 = s_x_2 * s_y - s_x * s_x_y

    try:
        a = round(delta_1 / delta, 3)
        b = round(delta_2 / delta, 3)
        result = lambda x: np.exp(b) * np.exp(a * x)
        function = f"{round(np.exp(b), 3)}e^({round(a, 3)}*x)"

        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)
    except Exception:
        a = b = function = s = sigma = result = None

    return {
        "name": "Экспоненциальная",
        "function": function,
        "lambda": result,
        "s": s,
        "sigma": sigma
    }


def log_app(points):
    n = len(points)

    for i in points:
        if i[0] <= 0:
            return {
                "name": "Логарифмическая",
                "function": None,
                "lambda": None,
                "s": None,
                "sigma": None
            }
    s_x = s_x_2 = s_y = s_x_y = 0
    for i in range(n):
        s_x += math.log(points[i][0])
        s_x_2 += math.log(points[i][0]) ** 2
        s_y += points[i][1]
        s_x_y += math.log(points[i][0]) * points[i][1]

    delta = s_x_2 * n - s_x ** 2
    delta_1 = s_x_y * n - s_x * s_y
    delta_2 = s_x_2 * s_y - s_x * s_x_y

    try:
        a = round(delta_1 / delta, 3)
        b = round(delta_2 / delta, 3)
        result = lambda x: a * np.log(x) + b

        function = f"{round(a, 3)} * ln(x) + {round(b, 3)}"

        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)
    except Exception:
        a = b = result = function = s = sigma = None

    return {
        "name": "Логарифмическая",
        "function": function,
        "lambda": result,
        "s": s,
        "sigma": sigma
    }


def degree_app(points):
    n = len(points)

    for i in points:
        if i[1] <= 0 or i[0] <= 0:
            return {
                "name": "Степенная",
                "function": None,
                "lambda": None,
                "s": None,
                "sigma": None
            }

    s_x = s_x_2 = s_y = s_x_y = 0
    for i in range(n):
        s_x += math.log(points[i][0])
        s_x_2 += math.log(points[i][0]) ** 2
        s_y += math.log(points[i][1])
        s_x_y += math.log(points[i][0]) * math.log(points[i][1])

    delta = s_x_2 * n - s_x ** 2
    delta_1 = s_x_y * n - s_x * s_y
    delta_2 = s_x_2 * s_y - s_x * s_x_y

    try:
        a = round(delta_1 / delta, 3)
        b = round(delta_2 / delta, 3)
        result = lambda x: math.exp(b) * (x ** a)

        function = f"{round(np.exp(b), 3)} * x^{round(a, 3)}"

        s = round(sum([(points[i][1] - result(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)
    except Exception:
        a = b = result = function = s = sigma = None

    return {
        "name": "Степенная",
        "function": function,
        "lambda": result,
        "s": s,
        "sigma": sigma
    }
