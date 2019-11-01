class BaseValidator:
    def __init__(self, value=None):
        self.value = value

    def validate(self):
        raise NotImplementedError()
