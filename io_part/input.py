from io_part import output as o
from math_part import own_functions

from termcolor import colored


def input_all_data():
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
        while True:
            try:
                a = float(input("Введите левую границу интегрирования: "))
                b = float(input("Введите правую границу интегрирования: "))
                if a > b:
                    o.print_error("Левая граница больше правой")
                else:
                    return a, b

            except ValueError:
                o.print_error("Некорректный формат ввода")

    func = input_function()
    a, b = input_border()
    e = input_accuracy()

    return {
        "function": func,
        "left_border": a,
        "right_border": b,
        "accuracy": e
    }


def input_method():
    input_str = "Выберите метод:\n"
    input_func_str = ""
    methods = [
        "Метод левых прямоугольников", "Метод правых прямоугольников", "Метод средних прямоугольников", "Метод трапеций"]
    for i in range(len(methods)):
        input_func_str = input_func_str + methods[i] + " | " + colored(str(i),
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
