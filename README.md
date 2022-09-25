# Welcome to Anagramble!

** Link to App Repository **
** Download link to presentation **

## Related Docs:

### Help File:

### Development Log (Source Control):

The 'log.txt' file denotes the git commits from the final commit down to the initial commit. The format of this document is the same as that within a terminal.

## Software Development Plan:

### Initial Pitch
The idea for the project was first pitched using the communication platform Discord to our assessors and support hub coordinators @ CoderAcademy for approval. The idea for Anagramble was accepted as within the scope of the project criteria, my ability at this stage to undertake said project, but also enough of a challenge to be rewarding and worthwhile. 

### Course of Development:

The development course was primarily done using Trello, an Agile-friendly software that allowed me to track individual items relevant to my project throughout. I was able to set dates that I wanted to complete certain assessment components, label the components as green (would-be-nice feature, low importance), yellow (important, but below time priority of red) and red (critical importance, most prioritized). Following this process allowed me to partake in stand-ups with substance behind my updates.

### Trello:

I have listed an example of how my Trello board looked during the development cycle.

![Trello](./images/Trello%2025.09.2022.jpg)

## Statement of Purpose and Scope
### Why?

As a passionate word puzzler, I was inspired to recreate a game similar to Countdown's 'Letter Round' where the user was given the choice to choose their letters and then be able to compete with the CPU for the longest word out of those letters.

Further, by making the game in the Terminal using Python logic, I have become more comfortable with using functions, classes, testing principles, error handling, packages and bash scripts.

### How does it work?

The user will choose to 'Play', view the rules or exit the game/execution. The user will choose the amount of rounds (1 to 5) and the difficulty of the CPU (Easy, Medium, Hard). The user will then choose 9 letters from vowels or consonants options. These letters form a list of which the user can make words from. The user can shuffle this list to see a different formation of the same letters. The user will have 3 guesses to make a word they are happy with, and can skip to the end if satisfied with a word they scored. The game tallies up the scores of the user and CPU by how long their word is and keeps a running total for the end. The user/computer with the highest points spread over the rounds wins the game. The user can then return to the main menu to play again or exit.

### Target Audience

The target audience of the program is future employers who would like to view my projects, my assessors at Coder Academy who will be marking the project against a rubric to see if I have met/failed to meet essential criteria and any wandering, word-puzzling souls who wish to play a fun anagram game! 

## User Features
### View Rules
The user can view the rules of the game at the main menu by selecting the 'Rules' option with the enter key (move with the arrow keys). These rules outline the way the game works from a user perspective and informs the user that there are certain rules that may arise during the game. 
### Choose Number of Rounds
Once the user has opted to 'Play', the user can set the number of rounds they would like to play from 1 to 5. The scores for the game are a running total of all individual round scores and not a 'Best of x' style game.
### Choose Difficulty
Once the user has opted to 'Pick Rounds', the user can set the difficulty of the CPU to Easy, Medium or Hard. The difficulty is an function that generates the possible words from the letters the user chooses, sorts them into word-length order and selects their word as a percentile of the possible list. For example, the Medium difficulty takes the word that is at the 65th percentile point on the index.
### Choosing vowels or consonants
Once the game has been set with the previous steps, the user can begin choosing vowels or consonants to form the 9 letter list. The user chooses a vowel with 'v' and a consonant with 'c'. There are maximums of 5 vowels and 6 consonants. If these limits are reached, the user must re-pick the other option until 9. 
### Shuffle Letters Option
When the letter list is prepared, it returns the same order of the list that user was picking vowels and consonants. If the user wishes to shuffle the letters to change their thinking perspective, they may do at this point by entering the 's' key at the word input stage.


## Logic Walkthrough

## Control Flow Diagram
![Flowchart](./images/Assignment%20Flowchart.jpg)
## Testing Permutations

| **PYTESTS**                                                                                                                                 |                                                                                                           |             |                    |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------|--------------------|
| **Feature**                                                                                                                                | **Expectation**                                                                                               | **Outcome**     | **Issues**             |
| Validate Word Function: Test word smaller than 3 letters returns False                                                                  | User inputs two letter word, thrown message and loses a guess                                             | As expected | SmallWordError     |
| Validate Word Function: Test word greater than or equal to 3 letters, in the dictionary, but not in letters returns False               | User inputs word that exists but not in letters, thrown relevant message and loses guess                  | As expected | InvalidLetterError |
| Validate Word Function: Test word greater than or equal to 3 letters, but not in dictionary returns False                               | User inputs word from letters that doesn't exist, thrown a message and loses a guess                      | As expected | GibberishError     |
| Validate Word Function: Test word greater than or equal to 3 letters, in dictionary and can be made with letters provided returns True  | User inputs valid word, accepted, score returned, loses a guess, can still improve on their word or break | As expected | Nil                |



## Installation Instructions

## PEP8

## Improvements