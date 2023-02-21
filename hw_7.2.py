"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _length = 5000  # длинна дороги в метрах
    _width = 20  # ширина дороги в метрах

    def asphalt_wieght(self, weight, layer_depth):
        self.weight = weight
        self.layer_depth = layer_depth
        return Road._width * Road._length * weight * layer_depth


cover_road = Road()
asph_weight = int(input('Введите вес асфальта на для покрытия 1 кв.м. толщиной 1 см в кг: '))
asph_depth = float(input('Введте толщину асфальта в м: '))
asph_value = int(cover_road.asphalt_wieght(asph_weight, asph_depth))
print(
    f'{cover_road._width}м*{cover_road._length}м*{asph_weight}кг*{asph_depth}м = {asph_value}кг = {asph_value // 1000}т')
