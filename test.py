import pytest
from Player import Human, Bot


def test_valid_input():
    human = Human("You")
    human.is_predictor = False
    assert human.validate_input("OO") == True
def test_valid_input_predictor():
    human = Human("You")
    human.is_predictor = True
    assert human.validate_input("OO2") == True


    
def test_valid_input_failed_letter_exceed(): # letters exceed
    human = Human("You")
    human.is_predictor = False
    assert human.validate_input("OO2") == False
def test_valid_input_failed_chars(): # letters are not in the form
    human = Human("You")
    human.is_predictor = False
    assert human.validate_input("CT") == False

def test_valid_input_failed_arbitrary_input(): # arbitrary input
    human = Human("You")
    human.is_predictor = True
    assert human.validate_input("chicken") == False
def test_valid_input_failed_predictor_chars(): # first two letters are not in the form
    human = Human("You")
    human.is_predictor = True
    assert human.validate_input("123") == False
def test_valid_input_failed_predictor_nums(): # last letter is not a number
    human = Human("You")
    human.is_predictor = True
    assert human.validate_input("CCC") == False
    
def test_valid_input_failed_predictor_num_not_in_range(): # last letter is not in range 0-4
    human = Human("You")
    human.is_predictor = True
    assert human.validate_input("CC9") == False