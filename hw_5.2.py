"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
user_num = int(input('Введите число: '))
even_sum = 0
odd_sum = 0


def num_cut(user_lst, even_num, odd_num):
    symb_num = user_lst % 10
    if (symb_num % 2) == 0:
        even_num += 1
    else:
        odd_num += 1
    if user_lst // 10 == 0:
        return even_num, odd_num
    return num_cut(user_lst // 10, even_num, odd_num)


even_sum, odd_sum = num_cut(user_num, even_sum, odd_sum)
print(f'Количество четных и нечетных цифр в числе равно: ({even_sum}, {odd_sum})')
