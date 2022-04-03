from io_part import output as o
from math_part import own_functions

from termcolor import colored


def input_all_data():
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
                if number < 1 or number > len(own_functions.functions):
                    o.print_error("Выбрано неверное число")
                else:
                    return number
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_function():
        input_str = "Выберите функцию:\n"
        input_func_str = ""
        for i in range(1, len(own_functions.functions) + 1):
            input_func_str = input_func_str + own_functions.functions[i]["function"] + " | " + colored(str(i),
                                                                                                       'yellow') + "\n"

        while True:
            try:
                number = int(input(input_str + input_func_str))
                if number < 1 or number > len(own_functions.functions):
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

    return {
        "method_number": method,
        "function": own_functions.functions[func]["value"],
        "left_border": a,
        "right_border": b,
        "accuracy": e,
        "mul": mul
    }
