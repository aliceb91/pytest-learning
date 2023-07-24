import pytest
from lib.password_checker import *

def test_return_true_when_equal():
    password_checker = PasswordChecker()
    result = password_checker.check("12345678")
    assert result == True

def test_return_true_when_greater():
    password_checker = PasswordChecker()
    result = password_checker.check("123456789")
    assert result == True

def test_return_error_when_short():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."