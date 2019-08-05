# pycommands
[![CircleCI](https://circleci.com/gh/rafaelcassau/pycommands.svg?style=shield)](https://circleci.com/gh/rafaelcassau/pycommands)
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
from commands.invoker import Invoker


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
running command: touch content.txt
running command: mv content.txt content-replaced.txt


# If a invoker.undo() is called then all commands undo operation will be done in the LIFO order.

invoker.undo()

# output
running undo command: mv content-replaced.txt content.txt
running undo command: rm content.txt


# If a invoker.execute() is called with run_undo as True, then the undo operation will be done always
# that a command raise CommandException

invoker = Invoker()

invoker.execute([
    Command1(),
    Command2(),
    InvalidCommand(),
], run_undo=True)

# output
running command: touch content.txt
running command: mv content.txt content-replaced.txt
running command: touch content.txt
running command: mv content.txt content-replaced.txt
running undo command: mv content-replaced.txt content.txt
running undo command: rm content.txt
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
