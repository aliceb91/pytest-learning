from lib.gratitudes import *

def test_returns_empty_array_when_empty():
    gratitudes = Gratitudes()
    result = gratitudes.gratitudes
    assert result == []

def test_returns_base_format():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_adds_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Makers for giving us this oppertunity")
    result = gratitudes.format()
    assert result == "Be grateful for: Makers for giving us this oppertunity"

def test_adds_double_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Makers for giving us this oppertunity")
    gratitudes.add("All the coaches for being amazing")
    result = gratitudes.format()
    assert result == "Be grateful for: Makers for giving us this oppertunity, All the coaches for being amazing"