import matplotlib.pyplot as plt
import numpy as np
from math_part import interpolate_methods as methods


def get_x(points):
    x = []
    for i in points:
        x.append(i[0])
    return x


def get_y(points):
    y = []
    for i in points:
        y.append(i[1])
    return y


def drawing_functions(source_function, points):
    plot_space = 2
    
    x = get_x(points)
    y = get_y(points)

    x_for_plot = np.linspace(np.min(x) - plot_space, np.max(x) + plot_space, 1000)

    if source_function is not None:
        plt.plot(x_for_plot, source_function(x_for_plot), linewidth=2.0, label="Исходная функция")

    for tmp_method in methods.methods:
        plt.plot(x_for_plot, [tmp_method[0](points, tmp_x) for tmp_x in x_for_plot], linewidth=2.0, label=tmp_method[1])

    plt.plot(x, y, 'o', label="Точки", color="black")

    plt.legend()
    plt.grid(True)

    plt.xlim(min(x) - plot_space, max(x) + plot_space)
    plt.ylim(min(y) - plot_space, max(y) + plot_space)
    plt.show()
