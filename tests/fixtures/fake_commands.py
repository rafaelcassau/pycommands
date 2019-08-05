from commands.base import BaseCommand
from commands.exceptions import CommandException


class Command1(BaseCommand):
    def build(self):
        return "touch content.txt"

    def build_undo(self):
        return "rm content.txt"


class Command2(BaseCommand):
    def build(self):
        return "mv content.txt content-replaced.txt"

    def build_undo(self):
        return "mv content-replaced.txt content.txt"


class InvalidCommand(BaseCommand):
    def build(self):
        raise CommandException()
