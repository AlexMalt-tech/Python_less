"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите число n: ")
temp_1 = n + n
temp_2 = n + n + n
n_sum = int(n) + int(temp_1) + int(temp_2) 
print(f'n + nn + nnn = {n_sum}' )