from io_part import output as o
from math_part import own_functions

from termcolor import colored


def input_mode():
    while True:
        try:
            m = int(input("Вы хотите вычислить интеграл функции с разрывом или без разрыва?" + colored(
                " (1 - без разрыва, 2 - с разрывом)\n", 'green')))
            if m != 2 and m != 1:
                o.print_error("Введено неверное число")
            else:
                return m
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_integrate_data(mode):
    def input_method():
        input_str = "Выберите метод:\n"
        input_func_str = ""
        methods = [
            "Метод левых прямоугольников", "Метод правых прямоугольников", "Метод средних прямоугольников",
            "Метод трапеций"]
        for i in range(len(methods)):
            input_func_str = input_func_str + methods[i] + " | " + colored(str(i + 1),
                                                                           'yellow') + "\n"

        while True:
            try:
                number = int(input(input_str + input_func_str))
                if number < 1 or number > len(own_functions.functions_without_break):
                    o.print_error("Выбрано неверное число")
                else:
                    return number
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_function():
        input_str = "Выберите функцию:\n"
        input_func_str = ""
        if mode == 1:
            for i in range(1, len(own_functions.functions_without_break) + 1):
                input_func_str = input_func_str + own_functions.functions_without_break[i][
                    "function"] + " | " + colored(
                    str(i),
                    'yellow') + "\n"
        else:
            for i in range(1, len(own_functions.functions_with_break) + 1):
                input_func_str = input_func_str + own_functions.functions_with_break[i]["function"] + " | " + colored(
                    str(i),
                    'yellow') + "\n"

        while True:
            try:
                number = int(input(input_str + input_func_str))
                if mode == 1:
                    if number < 1 or number > len(own_functions.functions_without_break):
                        o.print_error("Выбрано неверное число")
                    else:
                        return number
                else:
                    if number < 1 or number > len(own_functions.functions_with_break):
                        o.print_error("Выбрано неверное число")
                    else:
                        return number
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_accuracy():
        while True:
            try:
                e = float(input("Введите погрешность вычисления: "))
                if e <= 0:
                    o.print_error("Величина должна быть положительна")
                else:
                    return e
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_border():
        mul = 1
        while True:
            try:
                a = float(input("Введите левую границу интегрирования: "))
                b = float(input("Введите правую границу интегрирования: "))
                if a > b:
                    a, b = b, a
                    mul = -1

                return a, b, mul

            except ValueError:
                o.print_error("Некорректный формат ввода")

    method = input_method()
    func = input_function()
    a, b, mul = input_border()
    e = input_accuracy()

    if mode == 1:
        return {
            "method_number": method,
            "function": func,
            "left_border": a,
            "right_border": b,
            "accuracy": e,
            "mul": mul
        }
    else:
        return {
            "method_number": method,
            "function": func,
            "left_border": a,
            "right_border": b,
            "accuracy": e,
            "mul": mul
        }
