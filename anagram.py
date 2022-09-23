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
        vowel_counter = 0
        consonant_counter = 0
        while len(letter_list) < 9:
            user_input = input("Vowel or Consonant (v/c)? ")
            if user_input == 'c':
                if consonant_counter < 6:
                    letter_list.append(choose_consonant())
                    consonant_counter += 1
                else:
                    print("Maximum number of consonants is 6. Please pick a vowel.")
            elif user_input == 'v':
                if vowel_counter < 5:
                    letter_list.append(choose_vowel())
                    vowel_counter += 1
                else:
                    print("Maximum number of vowels is 5. Please pick a consonant.")
        
            nice_letter_list = ' '.join(letter_list)
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
            cpu_word = final_list[int(round(len(final_list) * 0.45))]
            cpu_score = len(cpu_word)
        elif self.difficulty == 'Medium':
            cpu_word = final_list[int(round(len(final_list) * 0.65))]
            cpu_score = len(cpu_word)
        elif self.difficulty == 'Hard':
            cpu_word = final_list[int(round(len(final_list) * 0.85))]
            cpu_score = len(cpu_word)
        return cpu_word, cpu_score

    def validate_word(self, user_input, letters):
        # Check if user input is made up of letters in letters list
        lt_list = letters.copy()
        if user_input in english_words_set:
            for letter in user_input:
                if letter not in lt_list:
                    return False
                else:
                    lt_list.pop(lt_list.index(letter))
            return True
        else:
            return False


    
        


# Function: Store input 3 times, tell user 3 guesses.
    def store_guesses(self, letters):
        guesses_remaining = 3
        guessed_words = []
        while guesses_remaining > 0:
                user_input = input("Enter your word: ")
                if self.validate_word(user_input, letters):
                    guesses_remaining -= 1
                    guessed_words.append(user_input)
                    print(f"'{user_input}' is a valid word for a score of {len(user_input)}. {guesses_remaining} guesses remaining.")
                elif user_input == '':
                    break
                else:
                    guesses_remaining -= 1
                    # TODO FIX ERROR HANDLING
                    print(f'{user_input} cannot be made from these letters or is not in the dictionary. {guesses_remaining} guesses remaining.')
        if not len(guessed_words):
            print('You haven\'t entered any valid words')
            return ""
        else:
            return max(guessed_words, key = len)
    
    def points_multipliers(self, guess, longest_word, cpu_score):
        if len(guess) == len(longest_word):
            print("Double points! Your word was the longest possible.")
            guess = guess + guess
        if cpu_score == len(longest_word):
            print('Darn! The computer got double points!')
            cpu_score = cpu_score * 2
        return guess, cpu_score


    def round_result(self, player_total, computer_total):
        if player_total > computer_total:
            print(f'You beat the CPU {player_total} to {computer_total}')
        elif player_total < computer_total:
            print(f'You lost to the CPU {player_total} to {computer_total}')
        else:
            print(f'You drew with the CPU {player_total} to {computer_total}')
        

    def final_result(self, player_running_total, cpu_running_total):
        if player_running_total > cpu_running_total:
            print(f"You won! You beat the CPU {player_running_total} to {cpu_running_total} in a game of {self.rounds}")
        elif player_running_total < cpu_running_total:
            print(f'You lost! You were defeated by the CPU {player_running_total} to {cpu_running_total} in a game of {self.rounds}')
        else:
            print(f'A tie! You drew with the CPU {player_running_total} to {cpu_running_total} in a best of {self.rounds}')

# Start function

    def start(self):
        player_running_total = 0
        cpu_running_total = 0
        for i in range(self.rounds):
            print(f" \n***Round {i + 1}***\n")
            letters = self.choose_letters()
            possible_words = self.possible_word_list(letters)
            cpu_word, cpu_score = self.cpu_score_calculator(possible_words)
            longest_word = possible_words[-1]
            print(f' \nThe longest word possible is {len(longest_word)} letters.\n')
            guess = self.store_guesses(letters)
            # End of Round
            print(f"\nYour best guess was: '{guess}'\n")
            guess, cpu_score = self.points_multipliers(guess, longest_word, cpu_score)
            print(f"\nThe computer's word was '{cpu_word}' for a score of {cpu_score} points.")
            print(f"\nThe longest word was '{longest_word}'\n")
            self.round_result(len(guess), cpu_score)
            print('\n')
            player_running_total += len(guess)
            cpu_running_total += cpu_score
        self.final_result(player_running_total, cpu_running_total)
        print('\n')
        input("Press Enter to return to the Main Menu ")
        os.system('clear')