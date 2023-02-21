"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 150, 'bonus': 70}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} - {self.position}')

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f'Данные рабочего: имя - {self.name}, фамилия - {self.surname}, должность - {self.position}, полный доход - {self.get_total_income()}'


man = Position()
man.name = 'Вася'
man.surname = 'Костин'
man.position = 'Грузчик'
print(man)
