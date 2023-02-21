"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    # атрибуты класса
    __color = ['red', 'yellow', 'green']

    # методы класса
    def running(self, light_color):
        while True:
            for el in light_color:
                print(f"{el}")
                if el == 'red':
                    sec_count = 7
                elif el == 'yellow':
                    sec_count = 2
                else:
                    sec_count = 5
                sleep(sec_count)


print('Для завешения программы нажмите Ctrl+C')
street_light = TrafficLight()
street_light.running(street_light._TrafficLight__color)
