"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/39-break-and-continue-statements-in-python

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/39-break-and-continue-statements-in-python

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/39-break-and-continue-statements"
                                 "-in-python")

    for x in range(1, 5):
        print('x = ', x)
        for y in range(1, 5):
            print('y = ', y)
            if x == y:
                print(f'\'x\' равен \'y\', и их значение: {x}, прерываем внутренний цикл')
                break

    x = 1
    while x < 5:
        print('x = ', x)
        y = 1
        while y < 5:
            print('y = ', y)
            if x == y:
                print(f'\'x\' равен \'y\', и их значение: {x}, прерываем внутренний цикл')
                break
            y += 1
        x += 1

    for x in range(1, 5):
        for y in range(1, 5):
            print(f'x = {x}, y = {y}')
            if 7 - x == y:
                print(f'Условие \'7 - x == y\' истинно, т.к. 7 - {x} == {y}. Прерываем внутренний цикл по y')
                break
        else:
            print(f'Цикл по y исчерпан. Условие \'7 - x == y\' ни разу не было истинным.')

    for x in range(1, 10):
        if x % 3 == 0:
            print(f'x = {x} и делится без остатка на 3. Продолжаем цикл с помощью continue.')
            continue
        print(f'x = {x} и не делится без остатка на 3.')

    x = 0
    while x < 9:
        x += 1
        if x % 3 == 0:
            print(f'x = {x} и делится без остатка на 3. Продолжаем цикл с помощью continue.')
            continue
        print(f'x = {x} и не делится без остатка на 3.')
