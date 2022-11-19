"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/45-python-working-with-datetime

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/45-python-working-with-datetime

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
import datetime


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/45-python-working-with-datetime")

    d = datetime.date
    dt = datetime.datetime
    print(f'Текущая дата: {d.today()}')
    print(f'Начало 2022 года: {datetime.date(2022, 1, 1)}')

    print(f'Текущая дата, без формата: {d.today().ctime()}')
    print(f'Текущая дата в формате \'%A, %d %b %Y\': {d.today().strftime("%A, %d %b %Y")}')
    print(f'Текущая дата в формате \'%d.%m.%Y\': {d.today().strftime("%d.%m.%Y")}')
    print(f'Текущая дата в формате \'%c\': {d.today().strftime("%c")}')
    print(f'Текущая дата в формате \'%x\': {d.today().strftime("%x")}')
    print(f'Текущая дата и время в формате \'%d.%m.%Y %H:%M:%S\': {dt.today().strftime("%d.%m.%Y %H:%M:%S")}')
    print(f'Текущее время в формате \'%H:%M:%S\': {dt.today().strftime("%H:%M:%S")}')
    print(f'Текущее время с микросекундами в формате \'%H:%M:%S.%f\': {dt.today().strftime("%H:%M:%S.%f")}')

    # Вывод текущего дня недели:
    # 0 - Понедельник
    # 1 - Вторник
    # 2 - Среда
    # 3 - Четверг
    # 4 - Пятница
    # 5 - Суббота
    # 6 - Воскресенье
    day = datetime.date(2022, 5, 21).weekday()
    days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    print(f'День недели, соответствующий 21 мая 2022 года: {days[day]}')

