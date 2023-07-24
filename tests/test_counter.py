from lib.counter import *

def test_return_0():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_add_once():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."

def test_add_twice():
    counter = Counter()
    counter.add(4)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 7 so far."
