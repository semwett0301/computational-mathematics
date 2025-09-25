from termcolor import colored
from instruments import input_output_instruments as io_ins


def input_parameters():
    mode = io_ins.input_mode()
    if mode == 'n':
        return io_ins.input_by_keyboard()
    else:
        return io_ins.input_by_file()


def print_matrix(printed_matrix):
    print('\nПреобразованная матрица')
    for i in range(len(printed_matrix)):
        s = ''
        for j in range(len(printed_matrix)):
            s += str(printed_matrix[i][j])
            s += ' '
        print(colored(s, 'green'))


def print_vector(name, vector):
    print('\n' + name)
    for elem in vector:
        print(colored(elem, 'green'))


def print_error(error):
    io_ins.print_error(error)
