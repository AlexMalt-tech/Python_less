class NonNegative:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value


class Worker:
    wage = NonNegative('wage')
    bonus = NonNegative('bonus')

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} - {self.position}'

    def get_total_income(self):
        return f'Total incom = {self.wage + self.bonus}'


OBJ = Position('Vasia', 'Ivanov', 'Docker', 100, 50)
print(OBJ.get_full_name())
print(OBJ.get_total_income())
