import numpy as np
from termcolor import colored

selection = np.array([-0.34, -0.73, 0.69, 0.55, 1.11, 0.62, 0.93, 0.42, 1, -0.48, -1.1, -0.66, -0.93, 0.42, -0.22, -0.11, -1.06, -0.72, -0.1, 1.05])
sort_selection = np.sort(selection)

print('Вариационный ряд:\n' + colored(str(sort_selection), 'green'))
print('Наименьшее значение (первая порядковая статистика)\n' + colored(str(sort_selection[0]), 'green'))
print('Наибольшее значение (n-ая порядковая статистика)\n' + colored(str(sort_selection[sort_selection.size - 1]), 'green'))
print('Размах\n' + colored(str(sort_selection[sort_selection.size - 1] - sort_selection[0]), 'green'))

mathematical_expectation = np.sum(sort_selection) / 20
average_deviation = (np.sum(sort_selection ** 2) / 20 - mathematical_expectation ** 2) ** 0.5




