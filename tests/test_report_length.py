from lib.report_length import *

def test_reported_length_equals_3():
    result = report_length("cat")
    assert result == "This string was 3 characters long."

def test_reported_length_equals_6():
    result = report_length("123456")
    assert result == "This string was 6 characters long."

def test_reported_length_equals_9():
    result = report_length("Different")
    assert result == "This string was 9 characters long."
