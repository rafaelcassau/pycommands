from commands.base import BaseCommand
from commands.exceptions import InvalidCommandParameter


class Command1(BaseCommand):
    def build(self):
        return "command 1"

    def build_undo(self):
        return "undo command 1"


class Command2(BaseCommand):
    def build(self):
        return "command 2"

    def build_undo(self):
        return "undo command 2"


class InvalidCommand(BaseCommand):
    def build(self):
        raise InvalidCommandParameter()
