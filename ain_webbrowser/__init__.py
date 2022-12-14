"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/47-python-opening-browser-url

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/47-python-opening-browser-url

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
import webbrowser
import sys


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/47-python-opening-browser-url")

    edge_executable_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    print(f'Путь к исполняемому файлу MS Edge: {edge_executable_path}')
    edge_browser_instance = webbrowser.BackgroundBrowser(edge_executable_path)
    webbrowser.register(name='edge', klass=None, instance=edge_browser_instance, preferred=False)

    try:
        inst = webbrowser.get('edge')
        inst.open_new("http://yandex.ru")  # Открыть страницу http://yandex.ru в браузере MS Edge
    except TypeError:
        typ, value, traceback = sys.exc_info()
        print(f'Error occurred:\r\n\ttype: {typ}\r\n\tvalue: {value}\r\n\ttraceback = {traceback}')

    webbrowser.open_new("http://python.org")
