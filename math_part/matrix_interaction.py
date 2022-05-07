from math_part import matrix_instruments as m_ins


def calculating_unknowns(matrix, results):
    m_ins.straight_running(matrix, results)
    if m_ins.calculating_determinant_in_triangle_matrix(matrix) != 0:
        return m_ins.reverse_running(matrix, results)
    return [0] * len(results)
