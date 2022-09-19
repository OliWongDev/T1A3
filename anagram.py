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

# Function: User chooses vowels or consonants to form 9 letter anagram puzzle 
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


# Function: Generate an ordered-by-length list of valid english words from the letters chosen by user. 
    def possible_word_list(letters):
        word_list = []
        for i in range(len(letters)):
            for x in list(permutations(letters, i)):
                y = " ".join(x)
                if len(y) and y in english_words_set:
                    word_list.append(y)
        final_list = helper.remove_duplicates(word_list)
        return final_list

# Function: Calculate CPU's length of word with word list.
    def cpu_score_calculator(final_list):
        if pick_difficulty() == 'Easy':
            cpu_word = final_list[round(len(final_list) * 0.25)]
            cpu_score = len(cpu_word)
        elif pick_difficulty() == 'Medium':
            cpu_word = final_list[round(len(final_list) * 0.5)]
            cpu_score = len(cpu_word)
        elif pick_difficulty() == 'Hard':
            cpu_word = final_list[round(len(final_list) * 0.8)]
            cpu_score = len(cpu_word)
        return cpu_score

# Function: Shuffle Letters with user input 'S'
# Function: Hint to longest word function with user input 'H'
    def hint_longest_word(self):
        longest_word_length = len(final_list[-1])
        return longest_word_length
        print(f'The longest word is {longest_word_length} letters.')

    
# User input words
# Function: Check word against english language
# Function: Store input 3 times, tell user 3 guesses.
# Tell user longest word

    def disclose_longest_word(self):
        longest_word = ''
        for word in final_list:
            if len(word) > len(longest_word):
                longest_word = word
        return longest_word
        print(f'The longest word was {len(longest_word)} letters: {longest_word}')

        
# Repeat loop for 2nd round. Store win/lose/draw.

# Final Screen "You won/lost/drew _ to _ against the CPU"
    def final_result(self):
        if player_total > computer_total:
            print(f"You beat the CPU {player_total} to {computer_total}")
        elif player_total < computer_total:
            print(f'You lost to the CPU {player_total} to {computer_total}')
        elif player_total == computer_total:
            print(f'You drew with the CPU {player_total} to {computer_total}')
        
# Play again or Quit

    