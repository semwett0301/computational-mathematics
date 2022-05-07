import math
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
        a = b = result_func = s = sigma = None

    return {
        "function": result_func,
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

    results_for_calc = [
        s_y,
        s_x_y,
        s_x_x_y
    ]

    a_0, a_1, a_2 = mi.calculating_unknowns(matrix, results_for_calc)

    if a_0 == a_1 == a_2 == 0:
        function = s = sigma = None
    else:
        function = f"{round(a_2, 3)}x^2 + {round(a_1, 3)}x + {round(a_0, 3)}"
        func_for_calc = lambda x: a_2 * x ** 2 + a_1 * x + a_0
        s = round(sum([(points[i][1] - func_for_calc(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)

    return {
        "function": function,
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

    results_for_calc = [
        s_y,
        s_x_y,
        s_x_2_y,
        s_x_3_y
    ]

    a_0, a_1, a_2, a_3 = mi.calculating_unknowns(matrix, results_for_calc)

    if a_0 == a_1 == a_2 == a_3 == 0:
        function = s = sigma = None
    else:
        function = f"{round(a_3, 3)}x^3 + {round(a_2, 3)}x^2 + {round(a_1, 3)}x + {round(a_0, 3)}"
        func_for_calc = lambda x: a_3 * x ** 3 + a_2 * x ** 2 + a_1 * x + a_0
        s = round(sum([(points[i][1] - func_for_calc(points[i][0])) ** 2 for i in range(n)]), 3)
        sigma = round(math.sqrt(s / n), 3)

    return {
        "function": function,
        "s": s,
        "sigma": sigma
    }