from itertools import permutations
from pick import pick
from english_words import english_words_set
import random
import helper
from letter_frequency import choose_consonant, choose_vowel
import os




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
        os.system('clear')
        print(nice_letter_list)
        return letter_list


## Function: Generate an ordered-by-length list of valid english words from the letters chosen by user. 
    def possible_word_list(self, letters):
        word_list = []
        for i in range(len(letters)):
            for x in list(permutations(letters, i)):
                y = "".join(x)
                if len(y) > 2 and y in english_words_set:
                    word_list.append(y)
        final_list = helper.remove_duplicates(word_list)
        print(final_list)
        return final_list

## Function: Calculate CPU's length of word with word list.
    def cpu_score_calculator(self, final_list):
        if self.difficulty == 'Easy':
            cpu_word = final_list[int(round(len(final_list) * 0.25))]
            cpu_score = len(cpu_word)
        elif self.difficulty == 'Medium':
            cpu_word = final_list[int(round(len(final_list) * 0.5))]
            cpu_score = len(cpu_word)
        elif self.difficulty == 'Hard':
            cpu_word = final_list[int(round(len(final_list) * 0.8))]
            cpu_score = len(cpu_word)
        return cpu_word, cpu_score

# Function: Shuffle Letters with user input 'S'
## Function: Hint to longest word function with user input 'H'
    
# User input words
# Function: Check word against english language

# Function: Store input 3 times, tell user 3 guesses.
    def store_guesses(self):
        guesses_remaining = 3
        guessed_words = []
        try:
            while guesses_remaining > 0:
                user_input = input("Enter your word: ")
                # TODO: Change conditional to reflect the selected letters on top of valid word.
                if user_input in english_words_set:
                    guesses_remaining -= 1
                    guessed_words.append(user_input)
                    print(f"'{user_input}' is a valid word for a score of {len(user_input)}. {guesses_remaining} guesses remaining.")
                elif user_input == '':
                    break
                else:
                    guesses_remaining -= 1
                    print(f'This word is not in the dictionary. {guesses_remaining} guesses remaining.')
            
            return max(guessed_words, key = len)
        except ValueError:
            print("Error: You haven't entered any words.")
            return self.store_guesses()

## Final Screen "You won/lost/drew _ to _ against the CPU"
    def final_result(self, player_total, computer_total):
        if player_total > computer_total:
            print(f"You beat the CPU {player_total} to {computer_total}")
        elif player_total < computer_total:
            print(f'You lost to the CPU {player_total} to {computer_total}')
        elif player_total == computer_total:
            print(f'You drew with the CPU {player_total} to {computer_total}')
        
## Home/Play Again or Quit
    def end_choice(choice):
       pass
            # Restart game from difficulty option
    

# Start function

    def start(self):
        for i in range(self.rounds):
            letters = self.choose_letters()
            possible_words = self.possible_word_list(letters)
            cpu_word, cpu_score = self.cpu_score_calculator(possible_words)
            longest_word = possible_words[-1]
            guess = self.store_guesses()
            # End of Round
            print(f"Your guess was: {guess}")
            print(f"The computer's word was {cpu_word} for a score of {cpu_score} points.")
            print(f"The longest word was {len(longest_word)} letters: {longest_word}.")

            self.final_result(len(guess), cpu_score)
    