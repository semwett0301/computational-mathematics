import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def plot_function(function, min_x, max_x, min_y, max_y, step):
    x = np.linspace(min_x, max_x, 10000)

    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.plot(x, function(x), "green", linewidth=1.5)

    ax.set(xlim=(min_x, max_x), xticks=np.arange(min_x, max_x, step),
           ylim=(min_y, max_y), yticks=np.arange(min_y, max_y, step))

    plt.show()


def plot_system(function1, function2):
    x, y = sp.symbols("x y")
    sp.plot_implicit(sp.Or(sp.Eq(function1(x, y), 0), sp.Eq(function2(x, y), 0)))
