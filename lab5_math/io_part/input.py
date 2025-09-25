import os

from termcolor import colored

from io_part import output as o
from math_part import functions as func


def input_source_mode():
    while True:
        try:
            mode = int(
                input("Вы хотите использовать функцию-пример или ввести узлы интерполяции? (1 - узлы, 2 - функция) "))
            if mode != 1 and mode != 2:
                o.print_error("Выбрано неверное число")
            else:
                return mode
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_file_mode():
    while True:
        try:
            mode = int(input("Вы хотите ввести узлы с файла или экрана? (1 - файл, 2 - экран) "))
            if mode != 1 and mode != 2:
                o.print_error("Выбрано неверное число")
            else:
                return mode
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_dots_by_file():
    points = []

    file = open(os.path.abspath(os.curdir) + '\\' + "input.txt", 'r')
    rows = file.read().split('\n')
    rows.remove('X Y')
    for i in rows:
        try:
            i = i.split(' ')
            points.append([float(i[0]), float(i[1])])
        except ValueError:
            o.print_error("Некорректный формат файла")
            return None

    return points


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


def input_number():
    while True:
        try:
            n = int(input("Введите число узлов: "))
            if n <= 0:
                o.print_error("Введите положительное число")
            else:
                return n
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_dots_by_screen(n):
    print("Введите координаты точек через пробел:")
    points = []

    for i in range(n):
        while True:
            tmp_dot = input().split(" ")
            if len(tmp_dot) != 2:
                o.print_error("Введено не два числа")
            else:
                try:
                    x = float(tmp_dot[0])
                    y = float(tmp_dot[1])
                    points.append([x, y])
                    break
                except ValueError:
                    o.print_error("Некорректный формат ввода")

    return points


def input_borders():
    while True:
        try:
            a = float(input("Введите левую границу интервала: "))
            b = float(input("Введите правую границу интервала: "))
            if a > b:
                a, b = b, a

            return a, b

        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_step():
    while True:
        try:
            n = float(input("Введите шаг: "))
            if n <= 0:
                o.print_error("Введите положительное число")
            else:
                return n
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_argument():
    while True:
        try:
            arg = float(input("Введите координату точки, в которой нужно найти значение функции: "))
            return arg
        except ValueError:
            o.print_error("Некорректный формат ввода")
