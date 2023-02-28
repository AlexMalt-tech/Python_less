"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

user_num = 0
secret_num = randint(0, 100)
count = 10


def gues_func(user_n, secret_n, try_count):
    user_n = int(input('Введите загаданное число: '))
    if user_n == secret_n:
        print(f'Вы угадали верно, загаданное число: {secret_n}')
        return
    elif user_n > secret_n:
        print(f'Ваше число больше чем нужно. Осталось {try_count - 1} попыток.')
    else:
        print(f'Ваше число меньше чем нужно. Осталось {try_count - 1} попыток.')

    if try_count == 1:
        print(f'Количетво попыток закончилось')
        return
    return gues_func(user_n, secret_n, try_count - 1)


gues_func(user_num, secret_num, count)
