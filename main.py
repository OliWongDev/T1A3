# from itertools import permutations
from english_words import english_words_set
from helper import pick_difficulty, start_menu, choose_rounds
from letter_frequency import choose_consonant, choose_vowel
from anagram import Anagram
import os
import sys


while True:
    option = start_menu()
    if option == 'Play':
        game = Anagram(choose_rounds(), pick_difficulty())
        game.start()
    elif option == 'Rules':
        print('\n')
        print(""" ** RULES **

        - The user will choose the amount of rounds in the game (1 to 5). 

        - The user will choose the difficulty of the CPU (Easy, Medium, Hard).

        - The user will choose vowels ('v') or consonants ('c') to form a 9 letter list.
            
            - The minimum vowels are 3.

            - The minimum consonants are 4. 

        - The user will need to form a valid English word from the 9 letters given and press 'Enter' to submit. The user has 3 guesses. 

        - The user loses a guess for both submitting a valid word or submitting an invalid word.

        - If the user is happy with the guess they have made, they can leave the input box blank and press 'Enter' to skip to the end.

        - The user gains points for that round depending on how long the word is e.g 'cart' is equal to 4 points.

        - The user wins if they have a higher total points than the computer at the end of all the rounds.
        
        """)
        input("Press 'Enter' to return to main menu. ")
        os.system('clear')
        continue
    elif option == 'Quit':
        sys.exit()
