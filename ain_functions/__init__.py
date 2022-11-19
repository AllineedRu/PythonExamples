"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/42-python-functions

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/42-python-functions

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/42-python-functions")
    x = input("Введите значение для x: ")
    # запуск функции с возвращаемым значением
    print(get_argument_description(x))

    # запуск функции без возвращаемого значения
    simple_func_without_return_type()

    # запуск функции с произвольным количеством параметров
    my_vararg_function(1, 2, 3, 4, "one", "two")
    my_vararg_function()

    print(f'Программа завершилась!')


def simple_func_without_return_type():
    print(f'Сегодня прекрасный день, не так ли?')


def my_vararg_function(*args):
    """Это пример функции, принимающей произвольное количество параметров"""
    if args is ():
        print('Вы не передали никаких параметров')
    elif len(args) > 0:
        print(f'Количество параметров, переданных в функцию: {len(args)}')
        for p in args:
            print(f'Параметр: {p}')


def get_argument_description(param=None):
    if isinstance(param, int) or isinstance(param, str):
        if isinstance(param, str):
            if param.isnumeric():
                param = int(param)
            else:
                return "Вы ввели не число, а что-то другое"
        if param > 0:
            return "Вы ввели положительное число"
        elif param == 0:
            return "Вы ввели ноль"
        elif param < 0:
            return "Вы ввели отрицательное число"
    else:
        return "Вы ввели не число, а что-то другое"
