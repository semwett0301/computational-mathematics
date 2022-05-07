from io_part import input as i, output as o
from math_part import approximate_functions as app

if i.input_file_mode() == 2:
    n = i.input_number()
    points = i.input_dots_by_screen(n)
else:
    points = i.input_dots_by_file()

if points is not None:
    o.output_appr_results(app.lin_app(points), 'Линейная')
    o.output_appr_results(app.squad_app(points), 'Квадратичная')
    o.output_appr_results(app.qub_appr(points), 'Кубическая')
