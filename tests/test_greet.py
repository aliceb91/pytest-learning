from lib.greet import *

def test_greet_returns_hello_alice():
    result = greet("Alice")
    assert result == "Hello, Alice!"
