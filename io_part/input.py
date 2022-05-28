from io_part import output as o
from math_part import functions as func
from termcolor import colored



def input_function():
    input_str = "Выберите функцию:\n"
    input_func_str = ""
    for i in range(1, len(func.functions) + 1):
        input_func_str = input_func_str + func.functions[i]["function"] + " | " + colored(str(i), 'yellow') + "\n"

    while True:
        try:
            number = int(input(input_str + input_func_str))
            if number < 1 or number > len(func.functions):
                o.print_error("Выбрано неверное число")
            else:
                return number
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_initial_parameter(message):
    while True:
        try:
            n = float(input(message))
            return n
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_positive_parameter(message):
    while True:
        try:
            n = float(input(message))
            if n <= 0:
                o.print_error("Введите положительное число")
            else:
                return n
        except ValueError:
            o.print_error("Некорректный формат ввода")
