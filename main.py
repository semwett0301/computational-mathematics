from io_part import input as i
from io_part import output as o
from math_part import approximate_functions as app

if i.input_file_mode() == 2:
    n = i.input_number()
    points = i.input_dots_by_screen(n)
else:
    points = i.input_dots_by_file()

if points is not None:
    approximation_results = [app.lin_app(points), app.squad_app(points), app.qub_appr(points), app.log_app(points),
                             app.exp_appr(points), app.degree_app(points)]

    min_sigma = None
    result_name = ''
    for elem in approximation_results:
        if elem['sigma'] is not None:
            if min_sigma is None:
                min_sigma = elem['sigma']
                result_name = elem['name']
            elif min_sigma > elem['sigma']:
                min_sigma = elem['sigma']
                result_name = elem['name']

    output_mode = i.input_print_mode()
    if output_mode == 2:
        for elem in approximation_results:
            o.output_appr_results_by_screen(elem)
        o.print_results_by_screen(min_sigma, result_name)
    else:
        a = 0

    o.plot_func(points, approximation_results[0]['lambda'], approximation_results[1]['lambda'], approximation_results[2]['lambda'],
                approximation_results[3]['lambda'], approximation_results[4]['lambda'], approximation_results[5]['lambda'])
