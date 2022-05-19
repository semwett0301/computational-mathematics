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


# конечные разности
def final_differences(y_values):
    final_diff = [y_values]
    for i in range(len(y_values) - 1):
        temp_fin_dif = []
        for j in range(len(final_diff[i]) - 1):
            diff = final_diff[i][j + 1] - final_diff[i][j]
            temp_fin_dif.append(diff)
        final_diff.append(temp_fin_dif)
    return final_diff


def create_factorial(n):
    result = []
    for i in range(n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        result.append(fact)
    return result


def stirling_method(points, x):
    n = len(points)
    if n % 2 == 0:
        return

    h = points[1][0] - points[0][0]
    for i in range(n - 1):
        if round(points[i + 1][0] - points[i][0], 8) != round(h, 8):
            return

    x_arr = [i[0] for i in points]
    y_arr = [i[0] for i in points]

    fin_diff = final_differences(y_arr)
    fact = create_factorial(len(y_arr))
    mid = len(y_arr) // 2
    t = (x - x_arr[mid]) / h
    result = y_arr[mid]

    for n in range(1, mid + 1):
        mul = 1
        for j in range(1, n):
            mul *= (t * t - j * j)
        result += 1 / fact[2 * n - 1] * t * mul * (
                    fin_diff[2 * n - 1][-(n - 1) + mid] + fin_diff[2 * n - 1][-n + mid]) / 2
        result += 1 / fact[2 * n] * (t ** 2) * mul * (fin_diff[2 * n][-n + mid])
    return result


def bessel_method(points, x):
    n = len(points)
    if n % 2 == 1:
        return

    points.sort(key=lambda elem: elem[0])
    for i in range(n - 1):
        if round(points[i + 1][0] - points[i][0], 8) != round(h, 8):
            return

    x_arr = [i[0] for i in points]
    y_arr = [i[0] for i in points]

    fin_diff = final_differences(y_arr)
    fact = create_factorial(len(y_arr))
    mid = (len(y_arr) - 2) // 2
    t = (x - x_arr[mid]) / h
    result = 0

    for n in range(0, mid + 1):
        mul = 1
        for j in range(1, n + 1):
            mul *= (t - j) * (t + j - 1)
        result += (1 / fact[2 * n]) * mul * (fin_diff[2 * n][-n + mid] + fin_diff[2 * n][-(n - 1) + mid]) / 2
        result += (1 / fact[2 * n + 1]) * (t - (1 / 2)) * mul * (fin_diff[2 * n + 1][-n + mid])
    return result


methods = [
    [lagrange_method, "Метод Лагранжа"],
    [gauss_method, "Метод Гаусса"],
    [stirling_method, "Метод Стирлинга"],
    [bessel_method, "Метод Бесселя"]
]
