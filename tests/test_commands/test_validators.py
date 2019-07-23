import pytest
from commands.validators import BaseValidator

def test_simple():
    with pytest.raises():
        assert BaseValidator(None).validate()
