from io_part import input as inp, output
from math_part import functions as func

interpolate_function = func.functions[inp.input_function()]["value"]
y0 = inp.input_initial_parameter("Введите y(x0): ")

a, b = inp.input_borders()

h = inp.input_positive_parameter("Введите шаг: ")
e = inp.input_positive_parameter("Введите точность: ")
