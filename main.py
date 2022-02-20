import input_output as io
import matrix_interaction as mi

matrix_size, matrix, results = io.input_parameters()

unknowns = mi.calculating_unknowns(matrix, results)
if unknowns != [0]:
    io.print_matrix(matrix)
    io.print_vector('Вектор неизвестных: ', unknowns)
    io.print_vector('Вектор невязок: ', mi.calculating_residuals(matrix, results, unknowns))
else:
    io.print_error("\nОпределитель  матрицы равен нулю\nМетод неприменим")





