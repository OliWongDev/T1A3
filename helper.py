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
    option, not_needed = pick(options, title)
    return option


def pick_difficulty():
    title = "Difficulty:"
    diff_options = ['Easy', 'Medium', 'Hard']
    diff_option, not_needed2 = pick(diff_options, title)
    return diff_option

# Remove duplicates function
def remove_duplicates(words):
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return result