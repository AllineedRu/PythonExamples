"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/20-python-range-function

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/20-python-range-function

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "allineed.ru"
__contact__ = "allineed.ru[at]gmail.com"
__copyright__ = "Copyright 2022, Allineed.Ru"
__date__ = "2022/11/19"
__deprecated__ = False
__email__ = "allineed.ru[at]gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Max Damascus"
__status__ = "Alpha"
__version__ = "0.0.1"

import ain_common


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/20-python-range-function")

    for i in range(5):
        print(f'Текущее число i = {i}')

    for i in range(2, 5):
        print(f'Текущее число i = {i}')

    for i in range(1, 11, 2):
        print(f'Текущее число i = {i}')

    for i in range(11, 1, -2):
        print(f'Текущее число i = {i}')

    for i in range(-1, -20, -5):
        print(f'Текущее число i = {i}')

    my_list = ['Это', 'элементы', 'простого', 'списка', 'на', 'Python']
    for i in range(len(my_list)):
        print(f'Значение элемента списка с индексом {i}: {my_list[i]}')

    print(range(1, 100))

    print(sum(range(5)))  # 0 + 1 + 2 + 3 + 4 = 10
