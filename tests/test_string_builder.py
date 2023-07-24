from lib.string_builder import *

def test_returns_empty_string():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""

def test_returns_empty_string_length():
    string_builder = StringBuilder()
    result = string_builder.size()
    assert result == 0

def test_returns_single_added_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.output()
    assert result == "Hello"

def test_returns_single_added_length():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.size()
    assert result == 5

def test_returns_double_added_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" world")
    result = string_builder.output()
    assert result == "Hello world"

def test_returns_double_added_length():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" world")
    result = string_builder.size()
    assert result == 11
