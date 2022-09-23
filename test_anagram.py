import pytest
import anagram



# def test_validate_word():
#     assert test_anagram.validate_word(self, test_input, letters, guesses_remaining) == False


class TestAnagram:
    def test_validate_word(self):
        test_input = ''
        test_letters = ['a', 'b', 'e', 't', 'i', 'm', 's', 'o', 'g']
        guesses_remaining = 3
        # Test word smaller than 3 letters returns False
        assert anagram.Anagram.validate_word(self, test_input, test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters but not in dictionary returns False
        assert anagram.Anagram.validate_word(self, 'abetimsog', test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters, in the dictionary, but not in the letters given returns False
        assert anagram.Anagram.validate_word(self, 'friend', test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters, in the dictionary and can be made with letters provided returns True
        assert anagram.Anagram.validate_word(self, 'abet', test_letters, guesses_remaining) == True 

