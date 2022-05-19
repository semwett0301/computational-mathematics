import math


def lagrange_method(points, x):
    result = 0
    for j in range(len(points)):
        num = 1
        den = 1
        for i in range(len(points)):
            if i != j:
                num = num * (x - points[i][0])
                den = den * (points[j][0] - points[i][0])
        result = result + points[j][1] * num / den
    return result


methods = [
    [lagrange_method, "Метод Лагранжа"]
]
