import os

from math_part import interpolate_methods as m

from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def print_result_of_interpolation(points, x):
    print()
    for method in m.methods:
        result = method[0](points, x)
        if result is not None:
            print(colored(method[1] + ": " + str(result), 'blue'))
        else:
            print(colored(method[1] + ": " + "нельзя вычислить", 'red'))