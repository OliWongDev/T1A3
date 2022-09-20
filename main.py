# from itertools import permutations
from english_words import english_words_set
from helper import pick_difficulty, start_menu
from letter_frequency import choose_consonant, choose_vowel
from anagram import Anagram

option = start_menu()
if option == 'Play':
    difficulty = pick_difficulty()
    letter_list = Anagram.choose_letters()


