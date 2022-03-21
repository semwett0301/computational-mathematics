from io_part import input as i, output as o, drawing
from math_part import own_functions as func, methods

input_data = i.input_all_data()

if input_data["mode"] == 1:
    function = func.single_functions[input_data["function"]]["value"]
    a, b = input_data["data"]["a"], input_data["data"]["b"]
    drawing.plot_function(function, -9, 9, -9, 9, 1)
    if input_data["method"] == 1:
        x, iter_count = methods.hord_method(function, a, b, input_data["fault"])
        if x is None or iter_count is None:
            o.print_error("Некорректно выбран отрезок - внутри отрезка отсутствует корень")
        else:
            if i.input_file_mode("сохранить в файл или вывести на экран?") == 2:
                o.output_single_results(x, function(x), iter_count)
            else:
                if not o.output_single_results_in_file(x, function(x), iter_count):
                    o.print_error("Файл невозможно открыть, поэтому данные будут выведены на экран")
                    o.output_single_results(x, function(x), iter_count)
    else:
        x, iter_count = methods.simple_iterations_method(function, a, b, input_data["fault"])
        if x is None or iter_count is None:
            o.print_error("Некорректно введены данные - достаточное условие сходимости не выполняется")
        else:
            if i.input_file_mode("сохранить в файл или вывести на экран?") == 2:
                o.output_single_results(x, function(x), iter_count)
            else:
                if not o.output_single_results_in_file(x, function(x), iter_count):
                    o.print_error("Файл невозможно открыть, поэтому данные будут выведены на экран")
                    o.output_single_results(x, function(x), iter_count)
else:
    func_1 = func.system_functions[input_data["functions"][0]]["value"]
    func_2 = func.system_functions[input_data["functions"][1]]["value"]
    drawing.plot_system(func_1, func_2)
    x, y, first_fault, second_fault, iter_counter = methods.neuton_method(func_1,
                                                                          func_2,
                                                                          input_data["data"]["x"],
                                                                          input_data["data"]["y"], input_data["fault"])
    if x is None:
        o.print_error("Выбор начальных приближений некорректен - итерационный процесс не сходится")
    else:
            if i.input_file_mode("сохранить в файл или вывести на экран?") == 2:
                o.output_system_results(x, y, first_fault, second_fault, iter_counter)
            else:
                if not o.output_system_results_in_file(x, y, first_fault, second_fault, iter_counter):
                    o.print_error("Файл невозможно открыть, поэтому данные будут выведены на экран")
                    o.output_system_results(x, y, first_fault, second_fault, iter_counter)

