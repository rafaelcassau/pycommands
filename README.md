# pycommands
[![CircleCI](https://circleci.com/gh/rafaelcassau/pycommands.svg?style=svg)](https://circleci.com/gh/rafaelcassau/pycommands)
[![Codecov](https://codecov.io/gh/rafaelcassau/pycommands/branch/master/graph/badge.svg)](https://codecov.io/gh/rafaelcassau/pycommands)
  
Handle a list of commands that should be executed easily and with undo support.

# How to use

## Install
pycommands is available on PyPI

```bash
pip install pycommands
```

## Basic usage

#### Definition of commands
```python
from commands.base import BaseCommand
from commands.exceptions import CommandException

class Command1(BaseCommand):
    def build(self):
        print("command 1")

    def build_undo(self):
        print("undo command 1")


class Command2(BaseCommand):
    def build(self):
        print("command 2")

    def build_undo(self):
        print("undo command 2")


class InvalidCommand(BaseCommand):
    def build(self):
        print("Starting Invalid command")
        try:
            assert 1 == 2
        except Exception as error:
            raise CommandException(error)
```

#### Simple default execution with success commands

```python
from commands.invoker import Invoker


invoker = Invoker()

invoker.execute([
    Command1(),
    Command2(),
], run_undo=False)

# output
command 1
command 2

# If a invoker.undo() is called then all commands undo operation will be done in the LIFO order.

invoker.undo()

# output
command 2
command 1

# If a invoker.execute() is called with run_undo as True, then the undo operation will be done always
# that a command raise CommandException

invoker = Invoker()

invoker.execute([
    Command1(),
    Command2(),
    InvalidCommand(),
], run_undo=True)

# output
command 1
command 2
Starting Invalid command
undo command 2
undo command 1
```
## How to contribute

We welcome contributions of many forms, for example:
- Code (by submitting pull requests)
- Documentation improvements
- Bug reports and feature requests

## Setting up for local development

We use pipenv to manage dependencies, so make sure you have it installed.

Creating environment
```bash
/<project-path>/pipenv install --python=3
```

Activing environment
```bash
/<project-path>/pipenv shell
```

Install pre-commit hooks:
```bash
pre-commit install
```

Run tests by evoking pytest:
```
pytest
```

That's it! You're ready from development
