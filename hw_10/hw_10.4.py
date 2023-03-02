"""
Задание 4.

Преобразовать слова 'разработка', 'администрирование', 'protocol',
'standard' из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

wrd = ['разработка', 'администрирование', 'protocol',
       'standard']
b_wrd = []
str_wrd = []

for el in wrd:
    b_wrd.append(el.encode())

print(b_wrd)

for el in b_wrd:
    str_wrd.append(el.decode())

print(str_wrd)
