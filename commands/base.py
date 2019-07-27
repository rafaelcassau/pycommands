class BaseCommand:
    def __init__(self):
        self.command = None
        self.undo_command = None

    def execute(self):
        self._validate()
        self.command = self.build()
        # TODO need execute command with subprocess module

    def _validate(self):
        validators = self.get_validators()
        for validator in validators:
            validator.validate()

    def build(self):
        raise NotImplementedError()

    def get_validators(self):
        return []

    def undo(self):
        self.undo_command = self.build_undo()
        if self.undo_command:
            pass
            # TODO need execute undo command with subprocess module

    def build_undo(self):
        return None
