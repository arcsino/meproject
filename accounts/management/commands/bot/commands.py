from re import compile
from typing import Callable

from tabulate import tabulate

_commands = {}


def resister_command(regex: str):
    def inner(func):
        reg = compile(regex)
        _commands[reg] = func

    return inner


def print_commands() -> None:
    rows = []
    for key, val in _commands.items():
        rows.append([key.pattern, str(val)])

    print(tabulate(rows))


def find_commands(message) -> Callable:
    for key, val in _commands.items():
        if key.search(message):
            return val
