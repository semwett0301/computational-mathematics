from io_part import input as i, output as o
from math_part import methods

input_data = i.input_all_data()
result, n = methods.integrate_function(input_data["function"], input_data["method_number"],
                                       input_data["left_border"], input_data["right_border"],
                                       input_data["accuracy"])
o.output_results(result, n, input_data["mul"])
