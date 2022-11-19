"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/40-python-pass-statement

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/40-python-pass-statement

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/40-python-pass-statement")

    # Раскомментируйте этот блок, если хотите посмотреть на "вечный цикл"
    #while True:
    #    pass    # Ожидание завершения программы с помощью прерывания от клавиатуры (Ctrl + C)

    x = 10
    for y in range(1, 20):
        if x % y == 0:
            pass    # Нужно подумать, что здесь написать, а пока тут просто pass
        else:
            pass    # Ещё одно место, которое надо будет проработать и написать здесь какой

    for i in range(1, 100):
        pass    # Нужно позже вернуться и написать здесь что-то, а пока просто pass...


class SomeEmptyClass:
    pass


def my_future_function():
    pass    # Эта функция будет проработана потом, а пока тут просто pass
