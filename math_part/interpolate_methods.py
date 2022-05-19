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


def check_points(points, n):
    h = points[1][0] - points[0][0]
    for i in range(n - 1):
        if round(points[i + 1][0] - points[i][0], 8) != round(h, 8):
            return
    return h


def gauss_method(points, x):
    def calculate_t_first(t, length):
        tmp = t
        k = 1
        for i in range(1, length):
            if i % 2 == 1:
                tmp *= (t - k)
            else:
                tmp *= (t + k)
                k += 1
        return tmp

    def calculate_t_second(t, length):
        tmp = t
        k = 1
        for i in range(1, length):
            if i % 2 == 1:
                tmp *= (t + k)
            else:
                tmp *= (t - k)
                k += 1
        return tmp

    n = len(points)
    h = check_points(points, n)
    if h is None:
        return

    y = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        y[i][0] = points[i][1]

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    if n % 2 == 1:
        a = n // 2
    else:
        a = n // 2 - 1

    result = y[a][0]
    t = (x - points[a][0]) / h
    if x > points[a][0]:
        for i in range(1, n):
            if n % 2 == 1:
                result += calculate_t_first(t, i) * y[int((n - i) / 2)][i] / math.factorial(i)
            else:
                result += calculate_t_first(t, i) * y[int((n - i - 1) / 2)][i] / math.factorial(i)
    elif x < points[a][0]:
        for i in range(1, n):
            if n % 2 == 1:
                result += calculate_t_second(t, i) * y[int((n - i - 1) / 2)][i] / math.factorial(i)
            else:
                result += calculate_t_second(t, i) * y[int((n - i - 2) / 2)][i] / math.factorial(i)

    return result


def get_diff(y):
    fin_diff = [y]
    for i in range(len(y) - 1):
        temp_fin_dif = []
        for j in range(len(fin_diff[i]) - 1):
            diff = fin_diff[i][j + 1] - fin_diff[i][j]
            temp_fin_dif.append(diff)
        fin_diff.append(temp_fin_dif)
    return fin_diff


def stirling_method(points, arg):
    n = len(points)
    if n % 2 == 0:
        return

    h = check_points(points, n)
    if h is None:
        return

    y = [i[1] for i in points]

    fin_diff = get_diff(y)
    middle = len(points) // 2
    t = (arg - points[middle][0]) / h
    result = points[middle][1]

    for step in range(1, middle + 1):
        mul = 1
        for j in range(1, step):
            mul *= (t * t - j * j)
        result += 1 / math.factorial(2 * step - 1) * t * mul * (
                fin_diff[2 * step - 1][-(step - 1) + middle] + fin_diff[2 * step - 1][-step + middle]) / 2
        result += 1 / math.factorial(2 * step) * (t ** 2) * mul * (fin_diff[2 * step][-step + middle])
    return result


def bessel_method(points, arg):
    n = len(points)
    if n % 2 == 1:
        return

    h = check_points(points, n)
    if h is None:
        return

    y = [i[1] for i in points]

    fin_diff = get_diff(y)
    middle = (len(points) - 2) // 2
    t = (arg - points[middle][0]) / h
    result = 0

    for step in range(0, middle + 1):
        if t != 0.5:
            mul = 1
            for j in range(1, step + 1):
                mul *= (t - j) * (t + j - 1)
            result += (1 / math.factorial(2 * step)) * mul * (fin_diff[2 * step][-step + middle] + fin_diff[2 * step][-(step - 1) + middle]) / 2
            result += (1 / math.factorial(2 * step + 1)) * (t - (1 / 2)) * mul * (fin_diff[2 * step + 1][-step + middle])
        else:
            mul = 1
            k = 1
            for j in range(1, step + 1):
                mul *= k
                k += 2
            result += (-1) ** step / 2 * mul ** 2 / (2 ** (2 * step)) / math.factorial(2 * step) \
                      * (fin_diff[2 * step][-step + middle] + fin_diff[2 * step][-(step - 1) + middle])
    return result


methods = [
    [lagrange_method, "Метод Лагранжа"],
    [gauss_method, "Метод Гаусса"],
    [stirling_method, "Метод Стирлинга"],
    [bessel_method, "Метод Бесселя"]
]
