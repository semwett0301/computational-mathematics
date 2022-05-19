from io_part import input as inp, output, drawing as draw
from math_part import functions as func, interpolate_methods as methods

interpolate_function = None

if inp.input_source_mode() == 1:
    if inp.input_file_mode() == 1:
        points = inp.input_dots_by_file()
    else:
        points = inp.input_dots_by_screen(inp.input_number())
else:
    interpolate_function = func.functions[inp.input_function()]["value"]
    a, b = inp.input_borders()
    points = func.get_points_from_function(interpolate_function, a, b, inp.input_step())

argument = inp.input_argument()

output.print_result_of_interpolation(points, argument)
draw.drawing_functions(interpolate_function, points)


