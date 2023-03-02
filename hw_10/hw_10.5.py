"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess

from chardet import detect


def ping_source(source):
    ARGS = ['ping', source]
    SC_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in SC_PING.stdout:
        result = detect(line)
        line = line.decode(result['encoding'])
        # print(f'{line} type - {type(line)}')
        print(line)


print(ping_source('yandex.ru'))
print('-------------------------------------')
print(ping_source('youtube.com'))
