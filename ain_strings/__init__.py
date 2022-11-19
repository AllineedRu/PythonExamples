"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/15-python-working-with-strings

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/15-python-working-with-strings

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
    ain_common.print_sample_name("https://allineed.ru/development/python-development/15-python-working-with-strings")

    print('Я строка')
    print("Я тоже строка!")
    print('Я строка, а внутри есть \'подстрока\', обособленная также одинарными кавычками, как и я сама')
    print("Не важно, как задана строка - через 'одинарные' или \"двойные\" кавычки. Python умеет экранировать любые "
          "кавычки внутри строки!")
    print('C:\some\path\in\my\system\some\name')
    print(r'C:\some\path\in\my\system\some\name')
    print("""Это пример
    текста, занимающего
    несколько строк
    """)
    print('''Это
    ещё один пример
    многострочного текста
    ''')
    print('Это' + ' пример' + " сцепления " + 'строк')
    print('Это' ' пример' ' автоматической сцепки' ' строковых литералов')

    s1 = ' ещё один'
    s2 = ', но уже с переменными, где необходим оператор +'
    print('Это' + s1 + ' пример' ' автоматической сцепки' ' строковых литералов' + s2)

    s = ('Строка, которую '
         'можно удобно перенести')
    print(s)

    some_string = 'Некоторая строка'
    print(some_string[0])

    some_string = 'Некоторая строка'
    print(some_string[-1])
    print(some_string[-2])

    some_string = 'Некоторая строка'
    print(some_string[0:9])

    some_string = 'Некоторая строка'
    print(some_string[:9])
    print(some_string[10:])

    #some_string = 'Некоторая строка'
    #some_string[2] = '?'   # это приведёт к ошибке, т.к. строки в Python неизменяемые (иммутабельны)

    s = ('Строка, которую '
         'можно удобно перенести')
    print("Длина строки '" + s + "' равна ")
    print(len(s))

    s = ('Строка, которую '
         'можно удобно перенести')
    # print("Длина строки '" + s + "' равна " + len(s))     # это приведёт к ошибке, т.к. len() возвращает целое

    # чтобы ошибки при сцепке строк не было, нужно использовать приведение к строке через функцию str():
    print("Длина строки '" + s + "' равна " + str(len(s)))
