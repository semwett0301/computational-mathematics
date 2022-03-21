import os

from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def output_single_results(x, value, iteration):
    print(colored("\nНайденный корень: " + str(x), 'blue'))
    print(colored("Значение в корне: " + str(value), 'blue'))
    print(colored("Количество итераций: " + str(iteration), 'blue'))


def output_system_results(x, y, fau_x, fau_y, iteration):
    print(colored("\nНайденный корень x: " + str(x), 'blue'))
    print(colored("Найденный корень y: " + str(y), 'blue'))
    print(colored("Вектор погрешностей: " + str(fau_x) + ", " + str(fau_y), 'blue'))
    print(colored("Количество итераций: " + str(iteration), 'blue'))


def output_single_results_in_file(x, value, iteration):
    try:
        file = open(os.path.abspath(os.curdir) + '\\' + "output.txt", 'w')
    except FileNotFoundError:
        print_error("Файл не может быть открыт")
        return False
    file.write(
        "Найденный корень: " + str(x) + "\n" + "Значение в корне: " + str(value) + "\n" + "Количество итераций: " + str(
            iteration) + "\n")
    file.close()
    return True


def output_system_results_in_file(x, y, fau_x, fau_y, iteration):
    try:
        file = open(os.path.abspath(os.curdir) + '\\' + "output.txt", 'w')
    except FileNotFoundError:
        print_error("Файл не может быть открыт")
        return False
    file.write("Найденный корень x: " + str(x) + "\n" + "Найденный корень y: " + str(y) + "\n" + "Вектор погрешностей: "
               + str(fau_x) + ", " + str(fau_y) + "\n" + "Количество итераций: " + str(iteration) + "\n")
    file.close()
    return True
