"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/17-python-working-with-lists

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/17-python-working-with-lists

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/17-python-working-with-lists")

    integer_list = [1, 2, 3, 4, 5, 6]
    print(integer_list)
    print(integer_list[2])
    print(integer_list[4:])
    print(integer_list[:])

    other_list = integer_list + [7, 8, 9, 10]
    print(other_list)

    integer_list[3] = 44
    print(integer_list)

    integer_list = [1, 2, 3, 4, 5, 6]
    print("Исходный список: " + str(integer_list))
    integer_list.append(7)
    integer_list.append(8)
    print("Изменённый список: " + str(integer_list))

    integer_list = [1, 2, 3, 4, 5, 6]
    print("Исходный список: " + str(integer_list))
    integer_list[1:4] = [22, 33, 44]
    print("Изменённый список: " + str(integer_list))

    integer_list[1:4] = []
    print("Список с удалёнными элементами: " + str(integer_list))

    integer_list = [1, 2, 3, 4, 5, 6]
    print("Исходный список: " + str(integer_list))
    integer_list[:] = []
    print("Очищенный список: " + str(integer_list))

    numbers = [1, 2, 3, 4]
    letters = ['a', 'b', 'c', 'd']
    mixed = [numbers, letters]
    print("Вложенные списки: " + str(mixed))
    print("Размер конечного списка: " + str(len(mixed)))
    print("Количество всех вложенных элементов: " + str(len(mixed[0]) + len(mixed[1])))

