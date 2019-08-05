from commands.invoker import Invoker

from tests.fixtures.fake_commands import Command1, Command2, InvalidCommand


def test_invoker_execute_should_execute_two_commands():
    commands_to_execute = [Command1(), Command2()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert len(invoker._executed_commands) == 2


def test_invoker_execute_should_execute_in_given_order():
    commands_to_execute = [Command2(), Command1()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert isinstance(invoker._executed_commands[0], Command2)
    assert isinstance(invoker._executed_commands[1], Command1)


def test_invoker_execute_should_execute_commands_in_giver_order():
    commands_to_execute = [Command1(), Command2()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert invoker._executed_commands[0].command == "touch content.txt"
    assert (
        invoker._executed_commands[1].command == "mv content.txt content-replaced.txt"
    )


def test_invoker_has_been_success_should_be_true():
    commands_to_execute = [Command1(), Command2()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert invoker.has_been_success is True


def test_invoker_has_been_success_should_be_false():
    commands_to_execute = [Command1(), Command2(), InvalidCommand()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert invoker.has_been_success is False


def test_invoker_undo_should_run_two_commands_in_reversed_order():
    commands_to_execute = [Command1(), Command2()]
    invoker = Invoker()
    invoker.execute(commands_to_execute)

    assert invoker._executed_commands[0].command == "touch content.txt"
    assert (
        invoker._executed_commands[1].command == "mv content.txt content-replaced.txt"
    )

    invoker.undo()

    assert (
        invoker._undo_commands_executed[0].undo_command
        == "mv content-replaced.txt content.txt"
    )
    assert invoker._undo_commands_executed[1].undo_command == "rm content.txt"


def test_invoker_execute_should_be_undo_automatically():
    commands_to_execute = [Command1(), Command2(), InvalidCommand()]
    invoker = Invoker()

    invoker.execute(commands_to_execute, run_undo=True)

    assert invoker._executed_commands[0].command == "touch content.txt"
    assert (
        invoker._executed_commands[1].command == "mv content.txt content-replaced.txt"
    )

    assert (
        invoker._undo_commands_executed[0].undo_command
        == "mv content-replaced.txt content.txt"
    )
    assert invoker._undo_commands_executed[1].undo_command == "rm content.txt"

    assert len(invoker._commands) == 3
    assert len(invoker._executed_commands) == 2
    assert len(invoker._undo_commands_executed) == 2


def test_invoker_execute_shouldnt_be_undo():
    commands_to_execute = [Command1(), Command2(), InvalidCommand()]
    invoker = Invoker()

    invoker.execute(commands_to_execute, run_undo=False)

    assert invoker._executed_commands[0].command == "touch content.txt"
    assert (
        invoker._executed_commands[1].command == "mv content.txt content-replaced.txt"
    )

    assert invoker._undo_commands_executed == []

    assert len(invoker._commands) == 3
    assert len(invoker._executed_commands) == 2
    assert len(invoker._undo_commands_executed) == 0
