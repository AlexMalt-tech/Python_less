"""
Задание 2.

Каждое из слов 'class', 'function', 'method' записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

# Способа запихать b' ' внутрь цикла не нашел, ни в материалах урока, ни в сети

wrd = ['class', 'function', 'method']

# вариант 1
for el in wrd:
    print(el.encode())
    print(type(el.encode()))
    print(len(el.encode()))

# вариант 2
print(f' {b"class"}, type: {type(b"class")}, length: {len(b"class")} ')
print(f' {b"function"}, type: {type(b"function")}, length: {len(b"function")} ')
print(f' {b"method"}, type: {type(b"method")}, length: {len(b"method")} ')

# вариант 3
for el in wrd:
    print(bytes(el, encoding='utf-8'))
    print(type(bytes(el, encoding='utf-8')))
    print(len(bytes(el, encoding='utf-8')))
