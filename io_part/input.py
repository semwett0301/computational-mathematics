import os

from termcolor import colored

from math_part import own_functions
from io_part import output as o


def input_file_mode(str):
    while True:
        try:
            mode = int(input("Вы хотите " + str + " (1 - файл, 2 - экран) "))
            if mode != 1 and mode != 2:
                o.print_error("Выбрано неверное число")
            else:
                return mode
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_all_data():
    def input_single_or_system():
        while True:
            try:
                mode = int(input("Вы хотите решить уравнение или систему уравнений? (1 - уравнение, 2 - система) "))
                if mode != 1 and mode != 2:
                    o.print_error("Выбрано неверное число")
                else:
                    return mode
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_single_method():
        methods = {
            1: "Метод хорд",
            2: "Метод простых итераций"
        }

        input_str = "Выберите метод:\n"
        for i in range(1, 3):
            input_str = input_str + methods[i] + " - " + str(i) + "\n"

        while True:
            try:
                number = int(input(input_str))
                if number != 1 and number != 2:
                    o.print_error("Выбрано неверное число")
                else:
                    return number
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_function():
        input_str = "Выберите функцию:\n"
        input_func_str = ""
        for i in range(1, len(own_functions.single_functions) + 1):
            input_func_str = input_func_str + own_functions.single_functions[i]["function"] + " | " + colored(str(i),
                                                                                                              'yellow') + "\n"

        while True:
            try:
                number = int(input(input_str + input_func_str))
                if number < 1 or number > len(own_functions.single_functions):
                    o.print_error("Выбрано неверное число")
                else:
                    return number
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_parameters():
        while True:
            try:
                a = float(input("Введите левую границу диапазона: "))
                b = float(input("Введите правую границу диапазона: "))
                if (a >= b):
                    o.print_error("Левая граница больше правой")
                else:
                    return a, b
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_fault():
        while True:
            try:
                e = float(input("Введите погрешность вычисления: "))
                if e <= 0:
                    o.print_error("Величина должна быть положительна")
                else:
                    return e
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_by_keyboard(function_data):
        if input_single_method() == 1:
            a, b = input_parameters()
            return {
                "mode": 1,
                "function": function_data,
                "method": 1,
                "data": {
                    "a": a,
                    "b": b
                },
                "fault": input_fault()
            }
        else:
            a, b = input_parameters()
            return {
                "mode": 1,
                "function": function_data,
                "method": 2,
                "data": {
                    "a": a,
                    "b": b,
                },
                "fault": input_fault()
            }

    def input_single_by_file(function_data):
        try:
            file = open(os.path.abspath(os.curdir) + '\\' + "input_single.txt", 'r')
            content = file.read().split("\n")
            variables = {}
            for element in content:
                element = element.split("=")
                variables[element[0]] = element[1]
            try:
                result = {
                    "mode": 1,
                    "function": int(function_data),
                    "method": int(variables["method"]),
                    "data": {
                        "a": float(variables["a"]),
                        "b": float(variables["b"])
                    },
                    "fault": float(variables["e"])
                }
                return result
            except Exception:
                return None
            finally:
                file.close()

        except Exception:
            return None

    # для системы

    def input_functions():
        input_str = "Выберите функции:\n"
        input_func_str = ""
        for i in range(1, len(own_functions.system_functions) + 1):
            input_func_str = input_func_str + own_functions.system_functions[i]["function"] + " | " + colored(str(i),
                                                                                                              'yellow') + "\n"

        while True:
            numbers_array = input(input_str + input_func_str).split(" ")
            numbers = []
            try:
                for i in range(len(numbers_array)):
                    numbers_array[i] = int(numbers_array[i])
            except ValueError:
                o.print_error("Некорректный ввод данных")
                continue

            if len(numbers_array) != 2:
                o.print_error("Нужно ввести два элемента")
                continue

            for number in numbers_array:
                if numbers.count(number) > 0:
                    continue
                else:
                    numbers.append(number)

            if len(numbers) != len(numbers_array):
                o.print_error("Присутствуют два одинаковых числа")
            else:
                return numbers

    def input_start_x():
        while True:
            try:
                x = float(input("Введите начальное приближение x: "))
                return x
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_start_y():
        while True:
            try:
                x = float(input("Введите начальное приближение y: "))
                return x
            except ValueError:
                o.print_error("Некорректный формат ввода")

    def input_system_by_keyboard(chosen_functions):
        return {
            "mode": 2,
            "functions": chosen_functions,
            "data": {
                "x": input_start_x(),
                "y": input_start_y()
            },
            "fault": input_fault()
        }

    def input_system_by_file(chosen_functions):
        try:
            file = open(os.path.abspath(os.curdir) + '\\' + "input_system.txt", 'r')
            content = file.read().split("\n")
            variables = {}
            for element in content:
                element = element.split("=")
                variables[element[0]] = element[1]
            try:
                result = {
                    "mode": 2,
                    "functions": chosen_functions,
                    "data": {
                        "x": float(variables["x"]),
                        "y": float(variables["y"])
                    },
                    "fault": float(variables["e"])
                }
                return result
            except Exception:
                return None
            finally:
                file.close()

        except Exception:
            return None

    if input_single_or_system() == 1:
        function = input_function()
        if input_file_mode("считать с файла или с экрана?") == 2:
            return input_by_keyboard(function)
        else:
            data = input_single_by_file(function)
            if data is None:
                o.print_error("При чтении файла возникла проблема. Данные будут считаны с клавиатуры")
                return input_by_keyboard(function)
            else:
                return data

    else:
        functions = input_functions()
        if input_file_mode("считать с файла или с экрана?") == 2:
            return input_system_by_keyboard(functions)
        else:
            data = input_system_by_file(functions)
            if data is None:
                o.print_error("При чтении файла возникла проблема. Данные будут считаны с клавиатуры")
                return input_system_by_keyboard(functions)
            else:
                return data
