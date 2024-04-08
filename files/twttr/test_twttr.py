from twttr import shorten

def test_shorten():
    assert shorten("saqibhassan") == ("sqbhssn")
def test_upper():
    assert shorten("SAQIBHASSAN") == ("SQBHSSN")
def test_numb():
    assert shorten("1saqib") == ("1sqb")
def test_punc():
    assert shorten("1.saqib") == ("1.sqb")