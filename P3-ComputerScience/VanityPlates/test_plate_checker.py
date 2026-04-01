import pytest
from plate_checker import is_valid

def test_is_valid_charlength():
    assert is_valid("CS50") == True, "CS50 Should be an accepted length"
    assert is_valid("C") == False, "C should be marked as too short"
    assert is_valid("CS5000000") == False, "CS5000000 should me marked as too long" 
    
def test_is_valid_first_chars_letters():
    assert is_valid("CS50") ==  True, "CS50 Should be accepted because its first 2 characters are letters"
    assert is_valid("C50") == False, "C50 should be marked as invalid because its first 2 characters are not letters"
    assert is_valid("5CS") == False, "5CS should be marked as invalid because its first 2 characters are not letters"
    

def test_is_valid_numbers_position():
    assert is_valid("CS50") == True, "CS50 should be accepted because its numbers are at the end and do not start with 0"
    assert is_valid("CS05") == False, "CS05 should be marked as invalid because its numbers start with 0"
    assert is_valid("CS50P") == False, "CS50P should be marked as invalid because its numbers are not at the end"
    

def test_is_valid_only_letters_and_numbers():
    assert is_valid("CS50") == True, "CS50 should be accepted because it only contains letters and numbers"
    assert is_valid("PI3.14") == False, "PI3.14 should be marked as invalid because it contains a period"
    assert is_valid("H$3") == False, "H$3 should be marked as invalid because it contains a dollar sign"
