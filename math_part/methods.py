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

    points.pop(len(points) - 1)

    return points


def milna_method(source_function, a, b, y0, h, e):
    def calculate_predicted(points):
        return points[num - 4][1] + 4 * h * \
            (2 * source_function(points[num - 3][0], points[num - 3][1]) - source_function(points[num - 2][0], points[num - 2][1])
                + 2 * source_function(points[num - 1][0], points[num - 1][1])) / 3

    def calculate_correct(points, y_predicted):
        return points[num - 2][1] + h * (source_function(points[num - 2][0], points[num - 2][1])
                                  + 4 * source_function(points[num - 1][0], points[num - 1][1])
                                  + source_function(points[num - 1][0] + h, y_predicted)) / 3

    x = a
    y = y0
    points = [[x, y]]
    count = 1
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
        count += 1
        if count == 4:
            break


    for num in range(4, int((b - a) / h) + 1):
        y_predicted = calculate_predicted(points)

        y_correct = calculate_correct(points, y_predicted)
        while abs(y_predicted - y_correct) > e:
            y_predicted = y_correct
            y_correct = calculate_correct(points, y_predicted)
        points.append((points[num - 1][0] + h, y_correct))
    return points


methods = [
    [euler_method, "Эйлера"],
    [milna_method, "Милна"]
]
