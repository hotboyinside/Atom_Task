# Задание 1
# проверю логи сервера(там можно найти описание проблемы)

# Задание 2

from collections.abc import Callable, Iterable


def create_handlers(callback: Callable) -> Iterable:
    handlers: Iterable = [lambda x=x: callback(x) for x in range(5)]
    return handlers


def execute_handlers(handlers: Iterable) -> None:
    for handler in handlers:
        handler()


# Задание 3
counter_tags = 0
counter_quotes2x = 0

with open('atom_site.html', 'r', encoding='utf-8') as file:
    file = file.read()
    for index, symbol in enumerate(file):
        if (symbol == "<") and file[index + 1] != '/':
            counter_tags += 1
        elif symbol == '"':
            counter_quotes2x += 1

    print(f'Всего тегов: {counter_tags}, всего атрибутов: {counter_quotes2x / 2}')


# Задание 4
import requests


def current_public_ip():
    response = requests.get('https://ifconfig.me/')
    public_ip = response.text
    return public_ip


print(current_public_ip())

# Задание 5
import re


def check_contrast_version(version_1: str, version_2: str) -> int:
    version_1 = [int(x) for x in re.sub(r'(\.0+)*$', '', version_1).split(".")]
    version_2 = [int(x) for x in re.sub(r'(\.0+)*$', '', version_2).split(".")]

    while len(version_1) != len(version_2):
        if len(version_1) > len(version_2):
            version_2.append(0)
        else:
            version_1.append(0)

    for index, num in enumerate(version_1):
        if num > version_2[index]:
            return 1

        elif num < version_2[index]:
            return -1

    return 0


print(check_contrast_version('5.6.7', '5.6.7.000'))