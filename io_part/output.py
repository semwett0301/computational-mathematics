from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def output_results(result, n, mul):
    print()
    print(colored("Значение интеграла: " + str(result * mul), 'blue'))
    print(colored("Число разбиения интервала интегрирования для достижения требуемой точности: " + str(n), 'blue'))


def output_break_results(result, mul):
    print()
    print(colored("Значение интеграла: " + str(result * mul), 'blue'))
