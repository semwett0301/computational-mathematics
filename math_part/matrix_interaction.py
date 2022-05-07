import math


def calculating_unknowns(matrix):
    n = len(matrix)
    e = 0.0000001
    vector_old_ans = [0] * n
    vector_ans = [0] * n
    diff = e + 1
    num = 0

    while diff > e:
        for i in range(n):
            summary = 0
            for j in range(n):
                if i != j:
                    summary += matrix[i][j] / matrix[i][i] * vector_ans[j]
            vector_ans[i] = matrix[i][n] / matrix[i][i] - summary
        for i in vector_ans:
            if i is None or i == math.inf or i == -math.inf:
                return [0] * n

        max_difference = 0.0
        for i in range(n):
            if abs(vector_old_ans[i] - vector_ans[i]) > max_difference:
                max_difference = abs(vector_old_ans[i] - vector_ans[i])
        diff = max_difference
        for i in range(n):
            vector_old_ans[i] = vector_ans[i]
        num += 1
    return vector_ans
