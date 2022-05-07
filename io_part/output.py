from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def output_appr_results(results, type_of_function):
    if 'r' in results:
        if results['r'] is None:
            print_error("\nНе удалось посчитать коэффициент Пирсона")
        else:
            print(colored("\nКоэффициент корреляции Пирсона: " + str(results['r']) + '\n', 'yellow'))

    if results['function'] is None:
        print_error(type_of_function + " аппроксимация не была выполнена - значения расходятся, невозможно найти ответ")
    else:
        print(colored(type_of_function + " аппроксимация была выполнена", 'green'))
        print(colored("Полученная функция: " + results['function']
                      + '\nS = ' + str(results['s']) + "\nsigma = " + str(results['sigma']) + '\n\n', 'blue'))
