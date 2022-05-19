import math


def lagrange_method(points, x):
    result = 0
    for i in range(len(points)):
        num = 1
        den = 1
        for j in range(len(points)):
            if i != j:
                num = num * (x - points[j][0])
                den = den * (points[i][0] - points[j][0])
        result = result + points[i][1] * num / den
    return result


def gauss_method(points, x):
    def calculate_t_first(t, length):
        tmp = t
        for i in range(1, length):
            if i % 2 == 1:
                tmp *= (t - i)
            else:
                tmp *= (t + i)
        return tmp

    def calculate_t_second(t, length):
        tmp = t
        for i in range(1, length):
            if i % 2 == 1:
                tmp *= (t + i)
            else:
                tmp *= (t - i)
        return tmp

    n = len(points)
    if n % 2 == 0:
        return
    points.sort(key=lambda elem: elem[0])
    h = points[1][0] - points[0][0]
    for i in range(n - 1):
        if round(points[i + 1][0] - points[i][0], 8) != round(h, 8):
            return

    y = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        y[i][0] = points[i][1]

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]


    result = y[int(n / 2)][0]
    t = (x - points[int(n / 2)][0]) / h
    if x > points[int(n / 2)][0]:
        for i in range(1, n):
            result += calculate_t_first(t, i) * y[int((n - i) / 2)][i] / math.factorial(i)
    elif x < points[int(n / 2)][0]:
        for i in range(1, n):
            result += calculate_t_second(t, i) * y[int((n - i - 1) / 2)][i] / math.factorial(i)

    return result


methods = [
    [lagrange_method, "Метод Лагранжа"],
    [gauss_method, "Метод Гаусса"]
]
