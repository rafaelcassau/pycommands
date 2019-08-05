from .exceptions import CommandException


class Invoker:
    def __init__(self):
        self._commands = []
        self._executed_commands = []
        self._undo_commands_executed = []

    def execute(self, commands, *, run_undo=False):
        self._commands = commands
        try:
            for command in commands:
                command.execute()
                self._executed_commands.append(command)
        except CommandException:
            if run_undo:
                self.undo()

    def undo(self):
        undo_list = reversed(self._executed_commands)
        for command in undo_list:
            command.undo()
            self._undo_commands_executed.append(command)

    @property
    def has_been_success(self):
        return self._executed_commands == self._commands
