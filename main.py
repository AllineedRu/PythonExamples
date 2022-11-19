"""
[EN] This is the main module for executing all the Python samples from the https://allineed.ru site
[RU] Это главный модуль для выполнения всех примеров на Python с сайта https://allineed.ru

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


import ain_tuples
import ain_webbrowser
import ain_json
import ain_functions
import ain_pass_statement
import ain_for_statement

if __name__ == '__main__':
    # [RU] Запускает пример из статьи "Как открыть страницу в браузере при помощи Python?"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/47-python-opening-browser-url
    # [EN] Runs example from the article "How to open the webpage in the browser with Python?"
    # [RU] Link to the article: https://allineed.ru/development/python-development/47-python-opening-browser-url
    ain_webbrowser.run_sample()

    # [RU] Запускает пример из статьи "Кортежи в Python"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/43-python-tuples
    # [EN] Runs example from the article "Tuples in Python"
    # [RU] Link to the article: https://allineed.ru/development/python-development/43-python-tuples
    ain_tuples.run_sample()

    # [RU] Запускает пример из статьи "Как работать с JSON в Python"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/48-python-working-with-json
    # [EN] Runs example from the article "How to work with JSON in Python"
    # [RU] Link to the article: https://allineed.ru/development/python-development/48-python-working-with-json
    ain_json.run_sample()

    # [RU] Запускает пример из статьи "Функции в Python"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/42-python-functions
    # [EN] Runs example from the article "Functions in Python"
    # [RU] Link to the article: https://allineed.ru/development/python-development/42-python-functions
    ain_functions.run_sample()

    # [RU] Запускает пример из статьи "Оператор pass в Python"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/40-python-pass-statement
    # [EN] Runs example from the article "'pass' statement in Python"
    # [RU] Link to the article: https://allineed.ru/development/python-development/40-python-pass-statement
    ain_pass_statement.run_sample()

    # [RU] Запускает пример из статьи "Оператор цикла for в Python"
    # [RU] Ссылка на статью: https://allineed.ru/development/python-development/19-python-for-statement
    # [EN] Runs example from the article "'for' cycle statement in Python"
    # [RU] Link to the article: https://allineed.ru/development/python-development/19-python-for-statement
    ain_for_statement.run_sample()
