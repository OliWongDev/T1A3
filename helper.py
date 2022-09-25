from pick import pick
def start_menu():
    title = """


     ___      .__   __.      ___       _______ .______          ___      .___  ___. .______    __       _______ 
    /   \     |  \ |  |     /   \     /  _____||   _  \        /   \     |   \/   | |   _  \  |  |     |   ____|
   /  ^  \    |   \|  |    /  ^  \   |  |  __  |  |_)  |      /  ^  \    |  \  /  | |  |_)  | |  |     |  |__   
  /  /_\  \   |  . `  |   /  /_\  \  |  | |_ | |      /      /  /_\  \   |  |\/|  | |   _  <  |  |     |   __|  
 /  _____  \  |  |\   |  /  _____  \ |  |__| | |  |\  \----./  _____  \  |  |  |  | |  |_)  | |  `----.|  |____ 
/__/     \__\ |__| \__| /__/     \__\ \______| | _| `._____/__/     \__\ |__|  |__| |______/  |_______||_______|
                                                                                                                


    """
    options = ['Play', 'Rules', 'Quit']
    option, _ = pick(options, title)
    return option

def show_rules():
    print('\n')
    print(""" ** RULES **

    - The user will choose the amount of rounds in the game (1 to 5). 

    - The user will choose the difficulty of the CPU (Easy, Medium, Hard).

    - The user will choose vowels ('v') or consonants ('c') to form a 9 letter list.
        
        - The minimum vowels are 3.

        - The minimum consonants are 4. 

    - The user will need to form a valid English word from the 9 letters given and press 'Enter' to submit. The user has 3 guesses. 

    - The user can shuffle the letters by entering the 's' key during their guesses.

    - The user loses a guess for both submitting a valid word or submitting an invalid word.

    - If the user is happy with the guess they have made, they can leave the input box blank and press 'Enter' to skip to the end.

    - The user gains points for that round depending on how long the word is e.g 'cart' is equal to 4 points.

    - The user wins if they have a higher total points than the computer at the end of all the rounds.
    
    """)

def pick_difficulty():
    title = "Difficulty:"
    diff_options = ['Easy', 'Medium', 'Hard']
    diff_option, _ = pick(diff_options, title)
    return diff_option

# Remove duplicates function
def remove_duplicates(words):
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return result


def pick_rounds():
    rounds_prompt = "How many rounds would you like to play?"
    rounds_options = [1, 2, 3, 4, 5]
    menu_choice, _  = pick(rounds_options, rounds_prompt)

    return menu_choice