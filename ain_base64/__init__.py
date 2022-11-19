"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/44-python-encoding-to-base64

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/44-python-encoding-to-base64

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
import base64


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/44-python-encoding-to-base64")

    e = base64.b64encode(b'Some text to be encoded into base64!')
    print(f'Закодированный в Base64 bytes-like объект: e = {e}')
    d = base64.b64decode(e)
    print(f'Раскодированный из Base64 bytes-like объект: d = {d}')

    print('-------')
    mystr = 'Python is beautiful and charming!'
    mystr_byt = bytes(mystr, 'utf-8')
    mystr_byt_encoded = base64.b64encode(mystr_byt)
    print(f'Закодированный в Base64 bytes-like объект: mystr_byt_encoded = {mystr_byt_encoded}')
    mystr_byt_decoded = base64.b64decode(mystr_byt_encoded)
    print(f'Раскодированный из Base64 bytes-like объект: mystr_byt_decoded = {mystr_byt_decoded}')
    mystr_decoded = str(mystr_byt_decoded, 'utf-8')
    print(f'Раскодированная Base64 строка: mystr_decoded = {mystr_decoded}')

    print('-------')
    russtr = 'Тестовая строка с кириллицей'
    russtr_byt = bytes(russtr, 'windows-1251')
    russtr_byt_encoded = base64.b64encode(russtr_byt)
    print(f'Закодированный в Base64 bytes-like объект: russtr_byt_encoded = {russtr_byt_encoded}')
    russtr_byt_decoded = base64.b64decode(russtr_byt_encoded)
    print(f'Раскодированный из Base64 bytes-like объект: russtr_byt_decoded = {russtr_byt_decoded}')
    russtr_decoded = str(russtr_byt_decoded, 'windows-1251')
    print(f'Раскодированная Base64 строка: russtr_decoded = {russtr_decoded}')
