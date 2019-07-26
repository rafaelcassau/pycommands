from commands.validators import BaseValidator

import pytest


def test_simple():
    with pytest.raises(NotImplementedError):
        assert BaseValidator(None).validate()
