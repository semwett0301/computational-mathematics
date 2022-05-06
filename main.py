from io_part import input as i

if i.input_file_mode() == 2:
    n = i.input_number()
    x_val, y_val = i.input_dots_by_screen(n)
else:
    x_val, y_val = i.input_dots_by_file()
    if not (x_val is None or y_val is None):
        a = 0
