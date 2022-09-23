# from itertools import permutations
from english_words import english_words_set
from helper import *
from letter_frequency import choose_consonant, choose_vowel
from anagram import Anagram
import os
import sys


while True:
    option = start_menu()
    if option == 'Play':
        game = Anagram(pick_rounds(), pick_difficulty())
        game.start()
    elif option == 'Rules':
        show_rules()
        input("Press 'Enter' to return to main menu. ")
        os.system('clear')
        continue
    elif option == 'Quit':
        sys.exit()
