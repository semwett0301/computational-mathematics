import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from termcolor import colored

selection = np.array([-0.34, -0.73, 0.69, 0.55, 1.11, 0.62, 0.93, 0.42, 1, -0.48, -1.1, -0.66, -0.93, 0.42, -0.22, -0.11, -1.06, -0.72, -0.1, 1.05])
sort_selection = np.sort(selection)

min = sort_selection[0]
max = sort_selection[sort_selection.size - 1]

print('Вариационный ряд:\n' + colored(str(sort_selection), 'green'))
print('\nНаименьшее значение (первая порядковая статистика)\n' + colored(str(min), 'green'))
print('Наибольшее значение (n-ая порядковая статистика)\n' + colored(str(max), 'green'))
print('Размах\n' + colored(str(max - min), 'green'))

mathematical_expectation = np.sum(sort_selection) / 20
average_deviation = (np.sum(sort_selection ** 2) / 20 - mathematical_expectation ** 2) ** 0.5

print('\nМатематическое ожидание:')
print(colored('%.3f' % mathematical_expectation, 'green'))
print('Cреднеквадратичное отклонение:')
print(colored('%.3f' % average_deviation, 'green'))

f_empire = []
for i in range(sort_selection.size):
    f_empire.append(i / sort_selection.size)
segments = ['(' + str(sort_selection[i]) + ';' + str(sort_selection[i + 1]) + ']' for i in range(sort_selection.size - 1)]
segments.insert(0, str('(-oo;' + str(sort_selection[0]) + '0]'))
frame = pd.DataFrame({'f(x)': f_empire, 'segment': segments})

print('\nЗначения эмпирической функции:')
print(colored(frame.set_index('f(x)'), 'green'))

plt.step(sort_selection, f_empire)
plt.show()

data_for_gist = int(1 + np.log2(sort_selection.size))
sns.histplot(sort_selection, kde=True, stat='density', bins=data_for_gist)
plt.show()

data_for_polygon = (max - min) / data_for_gist
y, edg = np.histogram(sort_selection, np.arange(min, max + 0.1, data_for_polygon))
centers = 0.5 * (edg[1:] + edg[:-1])
plt.plot(centers, y)
plt.xticks(edg)
plt.yticks(y)
plt.show()
