from lib.check_codeword import *

def test_check_codeword_is_right_when_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_is_close_when_house():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_is_close_when_mouse():
    result = check_codeword("mouse")
    assert result == "WRONG!"
