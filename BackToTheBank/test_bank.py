from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("  Hello  ") == 0
    assert value("Hi") == 20
    assert value("h") == 20
    assert value("Hey") == 20
    assert value("  Hi  ") == 20
    assert value("Good morning") == 100
    assert value("Welcome") == 100
    assert value("  Good morning  ") == 100