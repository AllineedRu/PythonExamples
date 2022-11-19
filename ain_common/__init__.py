"""
[EN] Common module with different useful functions that help to organize the
structure and execution for all the Python samples from https://allineed.ru site

[RU] Общий модуль с разлиными полезными функциями, которые помогают организовать
структуру и выполнение всех примеров на Python с сайта https://allineed.ru

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


def print_sample_name(article_link: str):
    """
        [EN] Prints the link to the corresponding article from https://allineed.ru site for particular script sample

        [RU] Выводит на экран ссылку на статью сайта https://allineed.ru, для которой подготовлен пример скрипта
    """
    print('')
    print(f'======================================================================================================')
    print(f'>>> [RU] Запуск примера из статьи: {article_link}')
    print(f'>>> [EN] Running the sample from the article: {article_link}')
    print(f'======================================================================================================')
