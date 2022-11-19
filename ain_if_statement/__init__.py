"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/18-python-if-statement

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/18-python-if-statement

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/18-python-if-statement")

    x = int(input("Пожалуйста, введите число: "))
    if x < 0:
        print("Вы ввели отрицательное число")
    elif x == 0:
        print("Вы ввели 0")
    elif x > 0:
        print("Вы ввели положительное число")

    x = int(input("Пожалуйста, введите число: "))
    if x * 2 > 50:
        print("Результат умножения введённого числа на 2 больше 50!")
    else:
        print("Результат умножения введённого числа на 2 меньше 50!")

    x = int(input("Пожалуйста, введите число: "))
    if x * 2 > 50:
        print("Результат умножения введённого числа на 2 больше 50!")
    elif 0 <= x * 2 <= 50:
        print("Результат умножения введённого числа на 2 больше нуля и меньше или равен 50!")
    else:
        print("Результат умножения введённого числа на меньше нуля!")
