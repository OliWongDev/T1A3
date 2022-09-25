import os
import sys
from helper import *
from anagram import Anagram


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
