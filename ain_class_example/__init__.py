"""
[EN] Module contains the sample Python code from the article
https://allineed.ru/development/python-development/94-python-classes-basics

[RU] Модуль содержит пример Python кода из статьи
https://allineed.ru/development/python-development/94-python-classes-basics

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
__date__ = "2023/10/31"
__deprecated__ = False
__email__ = "allineed.ru[at]gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Max Damascus"
__status__ = "Alpha"
__version__ = "0.0.1"

import ain_common
from ain_class_example.robot import Robot


def run_sample():
    ain_common.print_sample_name("https://allineed.ru/development/python-development/94-python-classes-basics")

    # вывести информацию о предназначении класса Robot на экран консоли
    print(Robot.__doc__)

    # создать экземпляр робота со следующими параметрами:
    # количество рук: 2, количество ног: 2, высота (метров): 2.5, вес (кг): 1500, текущая скорость (км/ч): 0
    robot1 = Robot("Робот прямоходящий", 2, 2, 2.5, 1500, 0)

    # показать информацию об экземпляре созданного робота
    robot1.show_info()

    # вызвать метод прыжка у робота
    robot1.jump()

    # вызвать метод ходьбы для робота. Сразу пойти роботу не удастся, поскольку его текущая скорость равна 0
    robot1.walk()

    # установить скорость для робота 5 км/ч
    robot1.set_walk_speed(5)

    # вызвать метод прыжка, когда робот идёт
    robot1.jump()

    # повторно показать информацию об экземпляре робота
    robot1.show_info()

    # вызвать метод бега для робота.
    robot1.run()

    # вызвать метод прыжка, когда робот бежит
    robot1.jump()

    # создаём второго робота
    robot2 = Robot(name="Робот-паук", arms=4, legs=6, height=1.5, weight=2500, walking_speed=30)

    # выводим информацию о втором роботе
    robot2.show_info()

    # изменили значение статической переменной running_speed_coefficient,
    # которая изменит скорость бега для всех роботов
    Robot.running_speed_coefficient = 2.5

    # повторно вывести информацию об обоих роботах, чтобы убедиться, что их
    # скорость бега теперь увеличена
    robot1.show_info()
    robot2.show_info()