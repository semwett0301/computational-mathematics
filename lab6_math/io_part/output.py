from termcolor import colored


def print_error(error):
    print(colored(error, 'red'))


def output_points(real_function, points, method_name):
    print(colored(f"\nТочки, полученные методом", "magenta"), colored(f"{method_name}", 'blue'))
    print(colored("\nX  Y  real_Y  delta_Y"))
    for point in points:
        print(colored(str(round(point[0], 8)) + "  " + str(round(point[1], 8)) + "  " + str(round(real_function(point[0]), 8)) + "  "
                      + str(round(abs(real_function(point[0]) - point[1]), 8)), "cyan"))