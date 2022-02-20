from instruments import matrix_instruments as m_ins


def calculating_unknowns(matrix, results):
    m_ins.straight_running(matrix, results)
    if m_ins.calculating_determinant_in_triangle_matrix(matrix) != 0:
        return m_ins.reverse_running(matrix, results)
    return [0]


def calculating_residuals(matrix, results, unknowns):
    residuals = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j] * unknowns[j]
        residuals.append(sum - results[i])
    return residuals
