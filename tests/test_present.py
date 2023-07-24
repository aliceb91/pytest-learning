import pytest
from lib.present import *

def test_single_present():
    present = Present()
    present.wrap("A present for you!")
    result = present.unwrap()
    assert result == "A present for you!"

def test_wrapping_double_wrapping_error():
    present = Present()
    present.wrap("A present for you!")
    with pytest.raises(Exception) as e:
        present.wrap("Have another present!")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrapping_empty_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_existing_present_is_preserved():
    present = Present()
    present.wrap("A present for you!")
    with pytest.raises(Exception) as e:
        present.wrap("Have another present!")
    result = present.unwrap()
    assert result == result