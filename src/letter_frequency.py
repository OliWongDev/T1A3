import random

consonants = ["b", "c", "d", "f", "g",
              "h", "j", "k", "l", "m",
              "n", "p", "q", "r", "s",
              "t", "v", "w", "x", "y", "z"]

consonant_weights = [1.49, 2.71, 4.32, 2.30, 2.03,
                     5.92, 0.10, 0.69, 3.98, 2.61,
                     6.95, 1.82, 0.11, 6.02, 6.28,
                     9.10, 1.11, 2.09, 0.17, 2.11, 0.07]

vowels = ["a", "e", "i", "o", "u"]
vowel_weights = [8.12, 12.0, 7.31, 7.68, 2.88]

# Function: Chooses and randomizes the consonants according to a scrabble frequency when user picks consonants.
def choose_consonant():
    return ''.join(random.choices(consonants, weights=consonant_weights, k=1))

# Function: Chooses and randomizes the vowels according to a scrabble frequency when user picks consonants.
def choose_vowel():
    return ''.join(random.choices(vowels, weights=vowel_weights, k=1))

