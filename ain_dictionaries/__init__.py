"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/49-python-working-with-dictionaries

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/49-python-working-with-dictionaries

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/49-python-working-with"
                                 "-dictionaries")

    # создали пустой словарь my_empty_dictionary
    my_empty_dictionary = {}
    # распечатали пустой словарь
    print(my_empty_dictionary)

    books_and_authors = {
        "Л. Н. Толстой": "Война и мир",
        "Ф. М. Достоевский": "Преступление и наказание",
        "А. С. Пушкин": "Евгений Онегин"}

    print(books_and_authors)

    process_phase = {1: "старт", 20: "инициализация", 40: "подготовка данных", 50: "загрузка данных", 100: "завершение"}
    print(process_phase)

    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(d)

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(coordinates_dict)

    # ======================================================================
    # Получение значений словаря по ключу
    # ======================================================================
    process_phase = {1: "старт", 20: "инициализация", 40: "подготовка данных", 50: "загрузка данных", 100: "завершение"}
    print(process_phase[1])
    print(process_phase[20])
    print(process_phase[40])
    print(process_phase[50])
    print(process_phase[100])

    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(d[1])
    print(d[4])

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(coordinates_dict[(0, 0)])
    print(coordinates_dict[(20, 0)])

    # ======================================================================
    # Добавление новых элементов в словарь
    # ======================================================================
    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(d[1])
    print(d[4])

    d[5] = 500  # добавили в словарь новую пару 5: 500
    d[6] = 600  # добавили в словарь новую пару 6: 600
    print(d[5])  # вывели значение для ключа 5
    print(d[6])  # вывели значение для ключа 6

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(coordinates_dict[(0, 0)])
    print(coordinates_dict[(20, 0)])

    coordinates_dict[(20, 20)] = "20 по оси X, 20 по оси Y"  # добавили в словарь новую пару (20, 20) : "20 по оси X,
    # 20 по оси Y"
    coordinates_dict[(-10, 35)] = "-10 по оси X, 35 по оси Y"  # добавили в словарь новую пару (-10, 35) : "-10 по
    # оси X, 35 по оси Y"
    print(coordinates_dict[(20, 20)])  # вывели значение для ключа (20, 20)
    print(coordinates_dict[(-10, 35)])  # вывели значение для ключа (-10, 35)

    # ======================================================================
    # Замена значения в словаре для заданного ключа
    # ======================================================================
    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(d[1])
    print(d[4])

    d[1] = "сто"  # заменили значение для ключа 1
    d[2] = "двести"  # заменили значение для ключа 2
    print(d)  # вывели на экран содержимое всего словаря

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(coordinates_dict[(0, 0)])
    print(coordinates_dict[(20, 0)])
    coordinates_dict[(0, 0)] = "0 по оси X, 0 по оси Y"  # заменили значение для ключа (0, 0)
    coordinates_dict[(20, 0)] = "координаты (двадцать, ноль)"  # заменили значение для ключа (20, 0)
    print(coordinates_dict)  # вывели на экран содержимое всего словаря

    # ======================================================================
    # Удаление элементов из словаря
    # ======================================================================
    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(f'd до удаления d[1]: {d}')
    del d[1]
    print(f'd после удаления d[1]: {d}')

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(f'coordinates_dict до удаления coordinates_dict[(0, 0)]: {coordinates_dict}')
    del coordinates_dict[(0, 0)]
    print(f'coordinates_dict после удаления coordinates_dict[(0, 0)]: {coordinates_dict}')

    # ======================================================================
    # Получение всех ключей словаря
    # ======================================================================
    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(f'd: {d}')
    for dkey in list(d):
        print(dkey)

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(f'coordinates_dict: {coordinates_dict}')
    for coord_key in sorted(coordinates_dict):
        print(coord_key)

    # ======================================================================
    # Проверка наличия/отсутствия ключа в словаре - операторы in и not in
    # ======================================================================
    d = {1: 100, 2: 200, 3: 300, 4: 400}
    print(f'd: {d}')
    print(f'2 есть в словаре d? : {2 in d}')
    print(f'7 есть в словаре d? : {7 in d}')

    print()

    coordinates_dict = {(0, 0): "начальная точка", (20, 0): "20 по оси X", (0, 40): "40 по оси Y"}
    print(f'coordinates_dict: {coordinates_dict}')
    print(f'(50, 50) есть в словаре coordinates_dict? : {(50, 50) in coordinates_dict}')
    print(f'(0, 40) есть в словаре coordinates_dict? : {(0, 40) in coordinates_dict}')
    print(f'(1000, 2000) отсутствует в словаре coordinates_dict? : {(1000, 2000) not in coordinates_dict}')

    # ======================================================================
    # Другие полезные операции со словарями
    # ======================================================================
    print(dict([('раз', 1), ('два', 2), ('три', 3)]))  # выведет на консоль: {'раз': 1, 'два': 2, 'три': 3}

    print({x: x * 1000 for x in (10, 20, 30)})  # выведет на консоль: {10: 10000, 20: 20000, 30: 30000}

    mydict = dict(раз=1, два=2, три=3)
    print(mydict)  # выведет на консоль: {'раз': 1, 'два': 2, 'три': 3}
