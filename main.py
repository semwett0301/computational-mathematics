from io_part import input as inp, output as out, drawing
from math_part import functions as func, methods


func_number = inp.input_function()
source_function = func.functions[func_number]["value"]
real_function = func.functions[func_number]["solution"]

a, b, y0 = func.functions[func_number]["a"], func.functions[func_number]["b"], func.functions[func_number]["y0"]

h = inp.input_positive_parameter("Введите шаг: ")
e = inp.input_positive_parameter("Введите точность: ")

result_points = []
for method in methods.methods:
    result_points.append([method[0](source_function, a, b, y0, h, e), method[1]])
    out.output_points(real_function, result_points[len(result_points) - 1][0], result_points[len(result_points) - 1][1])
drawing.draw_functions(real_function, result_points)
