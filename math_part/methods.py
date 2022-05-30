from termcolor import colored

def euler_method(source_function, a, b, y0, h, e):
    x = a
    y = y0
    points = [[x, y]]
    while x <= b:
        new_y = y + h * source_function(x, y)
        new_y_h_2 = y + h * source_function(x, y) / 2
        new_y_h_2 += h * source_function(x + h / 2, new_y_h_2) / 2

        if abs(new_y - new_y_h_2) > e:
            h /= 2
            continue

        x += h
        y = new_y
        points.append([x, new_y])

    print(colored(h, 'red'))

    if points[-1][0] > b:
        points.pop(len(points) - 1)

    return points


def miln_method(source_function, a, b, y0, h, e):
    def calculate_predicted(points, h):
        return points[num - 4][1] + 4 * h * \
            (2 * source_function(points[num - 3][0], points[num - 3][1]) - source_function(points[num - 2][0], points[num - 2][1])
                + 2 * source_function(points[num - 1][0], points[num - 1][1])) / 3

    def calculate_correct(points, y_predicted, h):
        return points[num - 2][1] + h * (source_function(points[num - 2][0], points[num - 2][1])
                                  + 4 * source_function(points[num - 1][0], points[num - 1][1])
                                  + source_function(points[num - 1][0] + h, y_predicted)) / 3

    init_h = h
    init_x = x = a
    y = y0
    points = [[x, y]]
    while x <= b:
        new_y = y + h * source_function(x, y)
        new_y_h_2 = y + h * source_function(x, y) / 2
        new_y_h_2 += h * source_function(x + h / 2, new_y_h_2) / 2

        if abs(new_y - new_y_h_2) > e:
            h /= 2
            continue

        x += h
        y = new_y

        if x == init_x + init_h:
            points.append([x, new_y])
            init_x += init_h

        if len(points) == 4:
            break


    for num in range(4, int((b - a) / init_h) + 1):
        y_predicted = calculate_predicted(points, init_h)

        y_correct = calculate_correct(points, y_predicted, init_h)
        while abs(y_predicted - y_correct) > e:
            y_predicted = y_correct
            y_correct = calculate_correct(points, y_predicted, init_h)
        points.append((points[num - 1][0] + init_h, y_correct))

    return points


methods = [
    [euler_method, "Эйлера"],
    [miln_method, "Милна"]
]
