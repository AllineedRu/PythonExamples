"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/43-python-tuples

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/43-python-tuples

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/43-python-tuples")

    my_tuple = 100, 200, 300, 'это удивительно!'
    print(my_tuple)
    print(my_tuple[0])
    print(my_tuple[1])
    print(my_tuple[2])
    print(my_tuple[3])

    my_complex_tuple = my_tuple, ('это', 'ещё', 'один', 'кортеж')
    print(my_complex_tuple)

    # my_tuple[2] = 10000  # здесь будет ошибка, поскольку кортежи неизменяемые

    my_empty_tuple = ()
    print(f'Мой пустой кортеж: {my_empty_tuple}')

    # обратите внимание на запятую в конце. именно благодаря ей t
    # становится кортежем, а не строкой
    t = 'это кортеж, а не строка!',

    print(f'Проверка, что t - это кортеж, а не строка. t = {t}')

    t1 = 1000, 2000, 3000
    one, two, three = t1

    print(f'Кортеж t1: {t1}')
    print(f'Распакованные значения: one={one}, two={two}, three={three}')

    t1 = 1000, 2000, 3000  # "упаковка" кортежа t1 значениями 1000, 2000 и 3000
    # one, two, three, four = t1    # неверная "распаковка" кортежа t1 - переменная four уже лишняя
    # a, b = t1  # снова неверная "распаковка" кортежа t1 - переменных всего две, а не три
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list_tuple = (list1, list2, ['это', 'список', 'строк'])

    print(f'list_tuple = {list_tuple}')
    print(f'list_tuple[0] = {list_tuple[0]}')
    print(f'list_tuple[1] = {list_tuple[1]}')
    print(f'list_tuple[2] = {list_tuple[2]}')

    list1.reverse()
    list2.remove(4)

    list3 = list(list_tuple[2]);
    list3.append('ещё элемент')

    print(f'list_tuple[0] = {list_tuple[0]}')
    print(f'list_tuple[1] = {list_tuple[1]}')
    print(f'list_tuple[2] = {list_tuple[2]}')
