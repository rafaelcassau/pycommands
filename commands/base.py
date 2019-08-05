import logging
import subprocess
import sys
from subprocess import CalledProcessError, TimeoutExpired

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)


class BaseCommand:
    def __init__(self, timeout=60):
        self.command = None
        self.undo_command = None
        self.timeout = timeout

    def execute(self):
        self._validate()
        self.command = self.build()

        logger.info(f"running command: {self.command}")

        command = self.command.split()
        self._call(command)

    def build(self):
        raise NotImplementedError()

    def get_validators(self):
        return []

    def undo(self):
        self._validate()
        self.undo_command = self.build_undo()

        logger.info(f"running undo command: {self.undo_command}")
        if self.undo_command:
            command = self.undo_command.split()
            self._call(command)

    def build_undo(self):
        return None

    def _call(self, command):
        try:
            response = subprocess.run(
                command, capture_output=True, check=True, timeout=self.timeout
            )
            if response.stdout:
                logger.info(f"success: {response.stdout}")

        except CalledProcessError as error:
            logger.error(f"returned error: {error.stderr}")
        except TimeoutExpired as error:
            logger.error(f"returned error timeout: {error}")
        except Exception as error:
            logger.error(f"returned error: {error}")

    def _validate(self):
        validators = self.get_validators()
        for validator in validators:
            validator.validate()
