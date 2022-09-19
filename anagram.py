from itertools import permutations
from pick import pick
from english_words import english_words_set
import random
from helper import pick_difficulty, start_menu
from letter_frequency import choose_consonant, choose_vowel



class Anagram:

    def __init__(self, rounds, difficulty):
        self.rounds = rounds
        self.difficulty = difficulty


    def choose_letters(self):
        letter_list = []
        for letter in range(9):
            user_input = input("Vowel or Consonant (v/c)? ")
            if user_input == 'c':
                print("--> You picked a consonant!")
                letter_list.append(choose_consonant())
            elif user_input == 'v':
                print("--> You picked a vowel!")
                letter_list.append(choose_vowel())
        nice_letter_list = ' '.join(letter_list)
        print(nice_letter_list)
        return letter_list


# Function: Generate word list
    def possible_word_list(self):
        word_list = []
        
        return word_list
# Function: Calculate CPU's length of word with word list.
# Function: Shuffle Letters with user input 'S'
# Function: Hint to longest word function with user input 'H'
# User input words
# Function: Check word against english language
# Function: Store input 3 times, tell user 3 guesses.
# Tell user longest word
# Repeat loop for 2nd round. Store win/lose/draw.

# Final Screen "You won/lost/drew _ to _ against the CPU"
# Play again or Quit