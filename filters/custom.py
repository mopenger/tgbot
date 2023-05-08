from aiogram import types
from aiogram.dispatcher.filters import Filter, Command


class CommandNotInListFilter(Filter):
    def __init__(self, commands: Command):
        self.commands = commands


    def check(self, message: types.Message) -> bool:
        if not message.text.startswith('/'):
            return False
        return message.text[1:] in self.commands.commands
