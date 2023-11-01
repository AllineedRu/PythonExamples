"""
[EN] This script runs the example from the article
https://allineed.ru/development/python-development/94-python-classes-basics

[RU] Этот скрипт запускает пример из статьи
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


class Robot:
    """
    [RU] Класс, описывающий робота, у которого есть свойства: название робота (модель), количество рук,
    количество ног, высота робота (в метрах), вес робота (в килограммах), скорость ходьбы робота.
    [EN] A class that describes a robot that has specified properties: robot name (model), number of arms,
    number of legs, height of the robot (in meters), weight of the robot (in kilograms), walking speed of the robot.
    """
    __doc__ = "Robot - класс для создания экземпляров различных роботов"
    running_speed_coefficient: float = 1.5

    def __init__(self, name: str, arms: int, legs: int, height: int, weight: int, walking_speed: int):
        self.name: str = name
        self.arms: int = arms
        self.legs: int = legs
        self.height: int = height
        self.weight: int = weight
        self.walking_speed: int = walking_speed
        self._is_running: bool = False

    def _check_if_zero_speed(self, error_message_if_no_speed):
        """
        [RU] Закрытый метод класса Robot. Проверяет текущую скорость ходьбы робота и возвращает True, если она равна 0. В противном случае возвращает False;
        [EN] Private method of the Robot class. Checks the robot's current walking speed and returns True if it is 0. Otherwise returns False.

        :param error_message_if_no_speed: [RU] сообщение об ошибке, если скорость робота равна 0; [EN] error message if robot speed is 0
        :return: [RU] True, если скорость ходьбы робота равна 0, иначе False;
                 [EN] True if the robot's walking speed is 0, otherwise False.
        """
        if self.walking_speed == 0:
            print(error_message_if_no_speed)
            return True
        return False

    def walk(self):
        """
        [RU] Метод предписывает роботу начать движение (ходьбу) с текущей скоростью.
        Если текущая скорость робота равна 0, то будет показана ошибка;
        [EN] The method instructs the robot to start moving (walking) at the current speed.
        If the robot's current speed is 0, an error will be shown.
        """
        if not self._check_if_zero_speed(f'robot.walk(): Робот не может начать ходьбу, т.к. его скорость равна 0 км/ч'):
            print(f'robot.walk(): Робот пошёл со скоростью {self.walking_speed} км/ч')
            self._is_running = False

    def run(self):
        """
        [RU] Метод предписывает роботу начать бег с текущей скоростью ходьбы, умноженной на коэффициент
        running_speed_coefficient. Если текущая скорость робота равна 0, то будет показана ошибка;
        [EN] The method instructs the robot to start running at the current walking speed multiplied by the coefficient
        running_speed_coefficient. If the robot's current speed is 0, an error will be shown.
        """
        if not self._check_if_zero_speed(f'robot.run(): Робот не может начать бег, т.к. его скорость равна 0 км/ч'):
            print(f'robot.run(): Робот побежал со скоростью {self._get_run_speed()} км/ч')
            self._is_running = True

    def set_walking_speed(self, new_walking_speed: int):
        """
        [RU] Метод устанавливает скорость ходьбы для робота;
        [EN] The method sets the walking speed for the robot.

        :param new_walking_speed: [RU] новая скорость ходьбы для робота; [EN] new walking speed for the robot
        """
        self.walking_speed = new_walking_speed
        print(f'robot.set_speed({new_walking_speed}): Установлена новая скорость для робота: {self.walking_speed} км/ч')

    def _get_run_speed(self):
        """
        [RU] Закрытый метод. Возвращает текущую скорость бега робота;
        [EN] Private method. Returns the robot's current running speed.
        :return: [RU] значение текущей скорости бега робота; [EN] value of the robot's current running speed.
        """
        return self.walking_speed * self.running_speed_coefficient

    def jump(self):
        """
        [RU] Метод предписывает роботу прыгнуть, независимо от того, находится ли робот в движении или стоит;
        [EN] The method instructs the robot to jump, regardless of whether the robot is moving or standing.
        """
        if self.walking_speed == 0:
            print('robot.jump(): Робот подпрыгнул на месте.')
        elif self._is_running:
            print(f'robot.jump(): Робот подпрыгнул на бегу, двигаясь со скоростью {self._get_run_speed()} км/ч')
        else:
            print(f'robot.jump(): Робот подпрыгнул при ходьбе, двигаясь со скоростью {self.walking_speed} км/ч')

    def show_info(self):
        """
        [RU] Отобразить информацию о текущем экземпляре робота;
        [EN] Display information about the current robot instance
        """
        print('---')
        print('robot.show_info(): Вывод информации о текущем экземпляре класса Robot:')
        print(f'\tНазвание робота (модель): {self.name}')
        print(f'\tКоличество рук у робота: {self.arms}')
        print(f'\tКоличество ног у робота: {self.legs}')
        print(f'\tВысота робота (метров): {self.height}')
        print(f'\tВес робота (кг): {self.weight}')
        print(f'\tТекущая скорость ходьбы робота (км/ч): {self.walking_speed}')
        print(f'\tТекущая скорость бега робота (км/ч): {self._get_run_speed()}')
        print('---')
