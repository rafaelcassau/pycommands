from commands.base import BaseCommand

import pytest


def test_base_command_execute_should_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        BaseCommand().execute()


def test_base_command__validate_should_return_none():
    assert BaseCommand()._validate() is None


def test_base_command_build_should_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        BaseCommand().build()


def test_base_command_get_validators_should_return_empty_list():
    assert BaseCommand().get_validators() == []


def test_base_command_buid_undo_should_return_none():
    assert BaseCommand().build_undo() is None


def test_base_command_undo_should_return_none():
    assert BaseCommand().undo() is None
