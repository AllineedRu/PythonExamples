"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/19-python-for-statement

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/19-python-for-statement

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/19-python-for-statement")

    mylist = ["Это", "пример", "элементов", "списка", "и", "оператора", "for", "в", "Python"]
    for word in mylist:
        print(f'Элемент списка: {word}, длина элемента: {len(word)} символов')

    s = "Это пример использования цикла for в Python, который применяется к строке"
    cyr_symbols_count = 0
    lat_symbols_count = 0
    for ch in s:
        if ('А' <= ch <= 'Я') or ('а' <= ch <= 'я'):
            cyr_symbols_count += 1
        elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            lat_symbols_count += 1
    print(f'Количество кириллических символов в строке: {cyr_symbols_count}')
    print(f'Количество латинских символов в строке: {lat_symbols_count}')

    # Создаём простую последовательность
    fruits_and_vegetables = {'Апельсин': 'фрукт', 'Банан': 'фрукт', 'Огурец': 'овощ', 'Репа': 'овощ'}

    # Стратегия №1 - итерироваться по копии исходной последовательности
    for fav_name, fav_type in fruits_and_vegetables.copy().items():
        if fav_type == 'фрукт':
            del fruits_and_vegetables[fav_name]

    print(f'Результат стратегии №1: {fruits_and_vegetables}')

    fruits_and_vegetables = {'Апельсин': 'фрукт', 'Банан': 'фрукт', 'Огурец': 'овощ', 'Репа': 'овощ'}

    # Стратегия №2:  Создать новую коллекцию
    only_vegetables = {}
    for fav_name, fav_type in fruits_and_vegetables.items():
        if fav_type == 'овощ':
            only_vegetables[fav_name] = fav_type

    print(f'Результат стратегии №2: {only_vegetables}')
