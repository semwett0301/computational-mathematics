def swap_rows(matrix_for_swap, results, row1, row2):
    matrix_for_swap[row1], matrix_for_swap[row2] = matrix_for_swap[row2], matrix_for_swap[row1]
    results[row1], results[row2] = results[row2], results[row1]


def calculating_determinant_in_triangle_matrix(matrix_for_calculate):
    det = 1
    for i in range(0, len(matrix_for_calculate)):
        det *= matrix_for_calculate[i][i]
    return det


def straight_running(matrix, results):
    for i in range(len(matrix) - 1):
        swap_counter = i
        while matrix[i][i] == 0 and swap_counter < len(matrix):
            swap_rows(matrix, results, i, swap_counter)
            swap_counter += 1

        if swap_counter == len(matrix):
            return matrix, results

        for k in range(i + 1, len(matrix)):
            c = matrix[k][i] / matrix[i][i]
            matrix[k][i] = 0
            for j in range(i + 1, len(matrix)):
                matrix[k][j] = matrix[k][j] - c * matrix[i][j]
            results[k] = results[k] - c * results[i]
    return matrix, results


def reverse_running(matrix, results):
    unknowns = []
    for i in range(len(matrix) - 1, -1, -1):
        s = 0
        for j in range(i + 1, len(matrix)):
            s += matrix[i][j] * list(reversed(unknowns))[len(matrix) - j - 2]
        unknowns.append((results[i] - s) / matrix[i][i])
    return list(reversed(unknowns))
