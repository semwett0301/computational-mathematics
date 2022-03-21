from math_part import utils

def validate_hord(a, b, function):
    val_a = function(a)
    val_b = function(b)

    det_a = utils.calculate_det(function)
    det_b = utils.calculate_det(function)

    det_2_a = utils.calculate_det(det_a)
    det_2_b = utils.calculate_det(det_b)

    return val_a * val_b <= 0 and det_a(a) * det_b(b) >= 0 and det_2_a(a) * det_2_b(b) >= 0


def validate_simple_iterations(a, b, fi_function):
    return abs(utils.calculate_det(fi_function)(a)) <= 1 or abs(utils.calculate_det(fi_function)(b)) <= 1
