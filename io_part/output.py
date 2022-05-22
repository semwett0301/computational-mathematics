import os

import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def output_appr_results_by_screen(results):
    type_of_function = results['name']

    if 'r' in results:
        if results['r'] is None:
            print_error("\nНе удалось посчитать коэффициент Пирсона")
        else:
            print(colored("\nКоэффициент Пирсона: " + str(results['r']) + '\n', 'yellow'))

    if results['function'] is None:
        print_error(
            type_of_function + " аппроксимация не была выполнена - значения расходятся или некоторые точки не попадают в область определения функции.\n"
                               "Невозможно найти ответ")
    else:
        print(colored(type_of_function + " аппроксимация была выполнена", 'green'))
        print(colored("Полученная функция: " + results['function']
                      + '\nS = ' + str(results['s']) + "\nsigma = " + str(results['sigma']) + '\n\n', 'blue'))


def print_results_by_screen(min_sigma, name):
    print(colored(f"Лучшая аппроксимация: {name}", 'cyan'))
    print(colored(f"Лучшее СКО: {min_sigma}", 'cyan'))


def output_results_in_file(results, result_name, min_sigma):
    try:
        file = open(os.path.abspath(os.curdir) + '\\' + "output.txt", 'w')
        for elem in results:
            name = elem['name']

            if 'r' in elem:
                if elem['r'] is None:
                    file.write("Не удалось посчитать коэффициент Пирсона")
                else:
                    file.write("Коэффициент Пирсона: " + str(elem['r']) + '\n')

            if elem['function'] is None:
                file.write(
                    name + " аппроксимация не была выполнена - при поиске коэффициентов матрица их множителей имела нулевой определитель или некоторые точки не попадают в область определения функции.\n"
                           "Невозможно найти ответ\n\n")
            else:
                file.write(name + " аппроксимация была выполнена")
                file.write("\nПолученная функция: " + elem['function']
                                   + '\nS = ' + str(elem['s']) + "\nsigma = " + str(elem['sigma']) + '\n\n')

        file.write(f"Лучшая аппроксимация: {result_name}\n")
        file.write(f"Лучшее СКО: {min_sigma}")

        file.close()
    except FileNotFoundError:
        print_error("Файл не может быть открыт")


def plot_func(points, lin_app, sqd_app, qub_app, log_app, exp_app, deg_app):
    minimum_x = 0
    maximum_x = 0

    minimum_y = 0
    maximum_y = 0

    points_x = []
    points_y = []

    for i in points:
        maximum_x = max(i[0], maximum_x)
        minimum_x = min(i[0], minimum_x)
        maximum_y = max(i[1], maximum_y)
        minimum_y = min(i[1], minimum_y)
        points_x.append(i[0])
        points_y.append(i[1])

    x = np.linspace(minimum_x - 0.5, maximum_x + 0.5, 10000)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.plot(x, lin_app(x), "g", linewidth=2.0, label="linear")
    ax.plot(x, sqd_app(x), "r", linewidth=2.0, label="squad")
    ax.plot(x, qub_app(x), "b", linewidth=2.0, label="cube")
    if exp_app is not None:
        ax.plot(x, exp_app(x), "pink", linewidth=2.0, label="exp")
    x = np.linspace(0.000001, maximum_x + 0.5, 10000)
    if log_app is not None:
        ax.plot(x, log_app(x), "darkred", linewidth=2.0, label="log")
    if deg_app is not None:
        ax.plot(x, deg_app(x), "black", linewidth=2.0, label="deg")
    ax.legend()
    ax.plot(points_x, points_y, linewidth=0, marker=".", markersize=10, markeredgecolor="black",
            markerfacecolor="black")

    ax.set(xlim=(minimum_x - 1, maximum_x + 1), xticks=np.arange(minimum_x - 1, maximum_x + 1, 1),
           ylim=(minimum_y - 1, maximum_y + 1), yticks=np.arange(minimum_y - 1, maximum_y + 1, 1))

    plt.show()
