import os

from io_part import output as o


def input_file_mode():
    while True:
        try:
            mode = int(input("Вы хотите ввести данные с файла или экрана? (1 - файл, 2 - экран) "))
            if mode != 1 and mode != 2:
                o.print_error("Выбрано неверное число")
            else:
                return mode
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_number():
    while True:
        try:
            n = int(input("Введите число точек: "))
            if n <= 0:
                o.print_error("Введите положительное число")
            else:
                return n
        except ValueError:
            o.print_error("Некорректный формат ввода")


def input_dots_by_screen(n):
    print("Введите координаты точек через пробел:")
    x_val = []
    y_val = []

    for i in range(n):
        while True:
            tmp_dot = input().split(" ")
            if len(tmp_dot) != 2:
                o.print_error("Введено не два числа")
            else:
                try:
                    x = float(tmp_dot[0])
                    y = float(tmp_dot[1])
                    x_val.append(x)
                    y_val.append(y)
                    break
                except ValueError:
                    o.print_error("Некорректный формат ввода")

    return x_val, y_val


def input_dots_by_file():
    x_val = []
    y_val = []

    file = open(os.path.abspath(os.curdir) + '\\' + "input.txt", 'r')
    rows = file.read().split('\n')
    rows.remove('X Y')
    for i in rows:
        try:
            i = i.split(' ')
            x_val.append(float(i[0]))
            y_val.append(float(i[1]))
        except ValueError:
            o.print_error("Некорректный формат файла")
            return None, None

    return x_val, y_val
