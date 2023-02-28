class NonNegative:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")

        instance.__dict__[self.my_attr] = value


class Road:
    _length = 5000  # длинна дороги в метрах
    _width = 20  # ширина дороги в метрах
    weight = NonNegative('weight')
    layer_depth = NonNegative('layer_depth')

    def __init__(self, weight, layer_depth):
        self.weight = weight
        self.layer_depth = layer_depth

    def asphalt_wieght(self):
        return Road._width * Road._length * self.weight * self.layer_depth


asph_weight = int(
    input('Введите вес асфальта на для покрытия 1 кв.м. толщиной 1 см в кг: '))
asph_depth = float(input('Введте толщину асфальта в м: '))
cover_road = Road(asph_weight, asph_depth)

asph_value = int(cover_road.asphalt_wieght())

print(
    f'{cover_road._width}м*{cover_road._length}м*{asph_weight}кг*{asph_depth}м = {asph_value}кг = {asph_value // 1000}т')
