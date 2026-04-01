from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("bcdfgBCDFG") == "bcdfgBCDFG"
    assert shorten("Hello, World!") == "Hll, Wrld!"

    print("All tests passed!")