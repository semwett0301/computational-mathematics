from math_part import validation, utils


def hord_method(function, a, b, e):
    if validation.validate_hord(a, b, function):
        def compare_signs(first_param, second_param):
            return first_param * second_param > 0

        iter_count = 1

        if compare_signs(function(a), utils.calculate_second_det(function)(a)):
            x0 = a
            fixed = b
        else:
            x0 = b
            fixed = a

        x = x0 - (fixed - x0) / (function(fixed) - function(x0)) * function(x0)

        while abs(x - x0) > e:
            x0 = x
            x = x0 - (fixed - x0) / (function(fixed) - function(x0)) * function(x0)
            iter_count += 1

        return x, iter_count
    else:
        return None, None


def simple_iterations_method(function, a, b, e):
    det_a = utils.calculate_det(function)(a)
    det_b = utils.calculate_det(function)(b)
    if det_a > det_b:
        lam = - 1 / det_a
        last_x = a
    else:
        lam = - 1 / det_b
        last_x = b

    fi_function = lambda x: x + lam * function(x)

    if validation.validate_simple_iterations(a, b, fi_function):
        iter_count = 1
        curr_x = fi_function(a)

        q = utils.get_max_det_value(function, a, b)
        if q > 0.5:
            while abs(last_x - curr_x) > e:
                iter_count += 1
                last_x = curr_x
                curr_x = fi_function(last_x)
        else:
            while abs(last_x - curr_x) > (1 - q) * e / q:
                iter_count += 1
                last_x = curr_x
                curr_x = fi_function(last_x)

        return curr_x, iter_count
    else:
        return None, None


def neuton_method(function1, function2, x0, y0, e):
    iter_counter = 1
    last_x = x0
    last_y = y0

    jackobian = utils.calculate_jackobian(function1, function2, last_x, last_y)
    del_x = function1(last_x, last_y) / jackobian
    del_y = function2(last_x, last_y) / jackobian

    curr_x = last_x - del_x * utils.calculate_det_y(function2, last_x, last_y) + del_y * utils.calculate_det_y(
        function1, last_x, last_y)

    curr_y = last_y + del_x * utils.calculate_det_x(function2, last_x, last_y) - del_y * utils.calculate_det_x(
        function1, last_x, last_y)

    while abs(curr_x - last_x) > e or abs(curr_y - last_y) > e:
        iter_counter += 1
        last_x = curr_x
        last_y = curr_y
        jackobian = utils.calculate_jackobian(function1, function2, last_x, last_y)
        del_x = function1(last_x, last_y) / jackobian
        del_y = function2(last_x, last_y) / jackobian

        curr_x = last_x - del_x * utils.calculate_det_y(function2, last_x, last_y) + del_y * utils.calculate_det_y(
            function1, last_x, last_y)

        curr_y = last_y + del_x * utils.calculate_det_x(function2, last_x, last_y) - del_y * utils.calculate_det_x(
            function1, last_x, last_y)

        if iter_counter > 200:
            return None, None, None, None, None

    return curr_x, curr_y, abs(curr_x - last_x), abs(curr_y - last_y), iter_counter
