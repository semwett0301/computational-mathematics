from termcolor import colored
import os


def print_error(error):
    print(colored(error, 'red'))


def input_mode():
    mode = input("Хотите ли вы ввести данные из файла? (y/n) ")
    if mode != 'y' and mode != 'n':
        print_error("Некорректное значение")
        mode = input_mode()
    return mode


def input_size():
    try:
        size = int(input("Введите число строк матрицы: "))
    except ValueError:
        print_error("Некорректное значение")
        size = input_size()
    if size < 0 or size > 20:
        print_error("Некорректный диапазон")
        size = input_size()
    return size


def input_result():
    try:
        result = float(input("Введите результат данной строки: "))
    except ValueError:
        print_error("Некорректное значение")
        result = input_result()
    return result


def input_row(number_row, matrix_size):
    row = input("Введите " + str((number_row + 1)) + " строку матрицы: ")
    try:
        row = [float(x) for x in row.split()]
    except ValueError:
        print_error("Некорректные данные")
        row = input_row(number_row, matrix_size)
    if len(row) != matrix_size:
        print_error("Количество значений не совпадает с размером матрицы")
        row = input_row(number_row, matrix_size)

    return row


def input_by_keyboard():
    matrix_size = input_size()
    matrix = []
    results = []
    for number_row in range(matrix_size):
        matrix.append(input_row(number_row, matrix_size))
        results.append(input_result())

    return matrix_size, matrix, results


def input_by_file():
    path = input("Введите путь к файлу относительно текущей директории: ")

    global file
    try:
        file = open(os.path.abspath(os.curdir) + '\\' + path, 'r')
    except FileNotFoundError:
        print_error("Файл не найден или не может быть открыт")
        input_by_file()
    content = file.read().split('\n')

    matrix_size = 0
    try:
        matrix_size = int(content[0])
        if matrix_size < 0 or matrix_size > 20:
            print_error("Некорректное содержимое файла (размер матрицы выходит за границы)")
            file.close()
            exit(-1)
    except ValueError:
        print_error('Некорректное содержимое файла (размер матрицы не целое число)')
        file.close()
        exit(-1)

    matrix = []
    results = []
    for number_row in range(1, matrix_size + 1):
        content[number_row] = content[number_row].split(' | ')

        matrix.append(content[number_row][0])
        try:
            matrix[number_row - 1] = [float(x) for x in matrix[number_row - 1].split()]
            if len(matrix[number_row - 1]) != matrix_size:
                print_error("Размер строки " + str(number_row) + " не соответствует размеру матрицы")
                file.close()
                exit(-1)
        except ValueError:
            print_error("Строка матрицы A номер " + str(number_row) + " введена некорректно")
            file.close()
            exit(-1)

        results.append(content[number_row][1])
        try:
            results[number_row - 1] = float(results[number_row - 1])
        except:
            print_error("Результат строки номер " + str(number_row) + " введена некорректно")
            file.close()
            exit(-1)

    return matrix_size, matrix, results
