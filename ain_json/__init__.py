"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/48-python-working-with-json

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/48-python-working-with-json

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

import json
import ain_common


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/48-python-working-with-json")

    # сериализуем в JSON-строку список, содержащий внутри себя словарь
    json1_str = json.dumps(['one', 'two', 'three', {'somekey': ['someval1', 'someval2']}])
    print(f'JSON-строка json1_str: {json1_str}')

    # преобразуем кортеж в JSON-строку и выводим на консоль
    json2_str = json.dumps((1, 2, 3, 4, 5))
    print(f'JSON-строка json2_str: {json2_str}')

    # используем сортировку ключей и отступы для более красивого JSON-представления
    json3_str = json.dumps({'d': 'd_value', 'e': 'e_value', 'a': 'a_value'}, sort_keys=True, indent=4)
    print(f'JSON-строка json3_str: {json3_str}')

    # десериализация из JSON-строки в список, содержащий внутри себя, в частности, словарь
    json1_obj = json.loads(json1_str)
    print(f'json1_obj: {json1_obj}')
    print(f'json1_obj[0]: {json1_obj[0]}')
    print(f'json1_obj[1]: {json1_obj[1]}')
    print(f'json1_obj[2]: {json1_obj[2]}')
    print(f'json1_obj[3]: {json1_obj[3]}')
    print(f'json1_obj[3]["somekey"]: {json1_obj[3]["somekey"]}')
    print(f'json1_obj[3]["somekey"][0]: {json1_obj[3]["somekey"][0]}')
    print(f'json1_obj[3]["somekey"][1]: {json1_obj[3]["somekey"][1]}')

    # преобразуем JSON-строку в кортеж и выводим на консоль 3-й элемент кортежа
    json2_obj = json.loads(json2_str)
    print(f'json2_obj[2]: {json2_obj[2]}')

    # преобразуем JSON-строку в словарь и в цикле выводим элементы на консоль
    json3_obj = json.loads(json3_str)
    for k, v in dict(json3_obj).items():
        print(f'Итерируемся по словарю json3_obj: key = {k}, value = {v}')
