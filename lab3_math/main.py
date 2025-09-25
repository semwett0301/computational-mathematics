from io_part import input as i, output as o
from math_part import methods, own_functions as own

mode = i.input_mode()
input_data = i.input_integrate_data(mode)
if mode == 1:
    result, n = methods.integrate_non_break_function(own.functions_without_break[input_data["function"]]["value"],
                                                     input_data["method_number"],
                                                     input_data["left_border"], input_data["right_border"],
                                                     input_data["accuracy"])
    o.output_results(result, n, input_data["mul"])
else:
    result, n = methods.integrate_break_function(input_data["function"], input_data["method_number"],
                                                 input_data["left_border"], input_data["right_border"],
                                                 input_data["accuracy"])

    if result is None or n is None:
        o.print_error("Интеграл расходится, или функция не определена")
    else:
        o.output_break_results(result, input_data["mul"])
