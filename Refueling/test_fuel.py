import pytest
from fuel import convert, gauge
    

def test_convert():
    assert convert("0/1") == 0, "Expected 0 for 0/1"
    assert convert("1/4") == 25, "Expected 25 for 1/4"
    assert convert("1/2") == 50, "Expected 50 for 1/2"
    assert convert("3/4") == 75, "Expected 75 for 3/4"
    assert convert("1/1") == 100, "Expected 100 for 1/1"

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("abc")

def test_gauge():
    assert gauge(25) == "25%", "Expected '25%' for 25%"
    assert gauge(50) == "50%", "Expected '50%' for 50%"
    assert gauge(75) == "75%", "Expected '75%' for 75%"

    assert gauge(0) == "E", "Expected 'E' for 0%"
    assert gauge(1) == "E", "Expected 'E' for 1%"
    assert gauge(99) == "F", "Expected 'F' for 99%"
    assert gauge(100) == "F", "Expected 'F' for 100%"
    