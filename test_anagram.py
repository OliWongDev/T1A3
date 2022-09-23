import pytest
import anagram


class TestAnagram:
    def test_validate_word(self):
        test_letters = ['a', 'b', 'e', 't', 'i', 'm', 's', 'o', 'g']
        guesses_remaining = 3
        # Test word smaller than 3 letters returns False
        assert anagram.Anagram.validate_word(self, "at", test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters but not in dictionary returns False
        assert anagram.Anagram.validate_word(self, 'abetimsog', test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters, in the dictionary, but not in the letters given returns False
        assert anagram.Anagram.validate_word(self, 'friend', test_letters, guesses_remaining) == False
        # Test word is greater than or equal to 3 letters, in the dictionary and can be made with letters provided returns True
        assert anagram.Anagram.validate_word(self, 'abet', test_letters, guesses_remaining) == True

    def  test_choose_letters(self):
        consonant_counter = 0
        vowel_counter = 0
        user_input = ""
        letter_list = []
        # Test "v" entered when vowels are less than 5 adds a vowel to letter list
        #assert 
        # Test "c" entered when consonants are less than 6 adds a consonant to letter list

        # Test "v" entered when vowels are 5 or more does not add a vowel to letter list.

        # Test "c" when consonants are 6 or more does not add a consonant to letter list.



