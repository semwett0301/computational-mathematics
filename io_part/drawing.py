import matplotlib.pyplot as plt


def draw_functions(real_func, result_points):
    fig, ax = plt.subplots()
    for result_point in result_points:
        x = [a[0] for a in result_point[0]]
        y = [a[1] for a in result_point[0]]
        ax.plot(x, y, label=f"{result_point[1]}")

    ax.plot(x, [real_func(elem) for elem in x], label="Точное решение")
    ax.legend()

    ax.grid()
    plt.show()
