# from itertools import permutations
from english_words import english_words_set
from helper import pick_difficulty, start_menu
from letter_frequency import choose_consonant, choose_vowel
from anagram import Anagram
import os
import sys
while True:
    option = start_menu()
    if option == 'Play':
        game = Anagram(5, pick_difficulty())
        game.start()
    elif option == 'Rules':
        print("The rules are ...")
        input("Press Enter to return to main menu. ")
        os.system('clear')
        continue
    elif option == 'Quit':
        sys.exit()
