import os

from math_part import interpolate_methods as m

from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def print_result_of_interpolation(points, x):
    print()
    for method in m.methods:
        print(colored(method[1] + ": " + str(method[0](points, x)), 'blue'))