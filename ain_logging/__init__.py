"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/46-python-logging-module

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/46-python-logging-module

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
import logging
import datetime


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/46-python-logging-module")

    # получаем логгер для нашего модуля
    logger = logging.getLogger(__name__)

    # создаём хендлер для файла лога, кодировка файла будет UTF-8 для поддержки кириллических сообщений в логе
    fileHandler = logging.FileHandler(filename='application_log.log', encoding='utf-8')

    # задаём базовую конфигурацию логирования
    logging.basicConfig(format='[%(levelname)-10s] %(asctime)-25s - %(message)s', handlers=[fileHandler],
                        level=logging.INFO)

    # кортеж, содержащий дни недели. необходим для отражения дня, в который была запущена и завершилась программа
    days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')

    # получаем текущие дату и время в переменную now_dt
    now_dt = datetime.datetime.now()

    # получить точное наименование дня недели, в который запустился наш скрипт
    current_weekday = days[now_dt.weekday()]

    # формат для даты запуска/завершения скрипта
    date_format = "%d.%m.%Y %H:%M:%S.%f"

    # =======================================
    # Начало основной логики скрипта
    # =======================================
    logging.info(">>> Программа запущена. День: %s; Точная дата и время запуска: %s", current_weekday,
                 now_dt.strftime(date_format))

    # Запрашиваем ввод числа с клавиатуры
    user_input = input("Введите целое число от 0 до 100: ")

    # Проверяем, что было введено число, а не что-то иное
    if user_input.isnumeric():
        logger.info("Пользовательский ввод корректен. Введено число: %s", user_input)
        # преобразуем число, хранящееся в строке к настоящему число с типом int
        input_int_var = int(user_input)
        # проверяем диапазон, в котором находится число
        if input_int_var < 0 or input_int_var > 100:
            logger.error("Ошибка: введено некорректное число, выходящее за допустимый диапазон: %s", input_int_var)
            print(f'Ошибка, введено число, выходящее за допустимый диапазон.')
        elif input_int_var == 0:
            logger.warning("Предупреждение: пользователь ввёл 0")
            print(f'Вы ввели {input_int_var}. Ввод нуля допустим, но нежелателен, '
                  'т.к. операция деления на 0 число не будет выполнена.')
        else:
            print(f'Вы ввели {input_int_var}. Отличное число!')
            result = 100 / input_int_var
            print(f'Результат деления 100 / {input_int_var} = {100 / input_int_var}')
    else:
        # Если пользователь ввёл не число, то логируем ошибку в файл лога и выводим ошибку на консоль
        logger.error("Ошибка ввода: пользователь ввёл нечисловое значение!")
        print(f'Извините, ввод \'{user_input}\' не является корректным числом в допустимом диапазоне')

    # повторно получим текущие дату и время, чтобы отразить момент завершения скрипта в логе
    now_dt = datetime.datetime.now()
    # логируем запись о завершении программы
    logging.info("<<< Программа завершена. День %s; Точная дата и время завершения: %s", current_weekday,
                 now_dt.strftime(date_format))
