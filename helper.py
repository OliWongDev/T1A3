from pick import pick
def start_menu():
    title = "ANAGRAM GAME"
    options = ['Play', 'Rules', 'Quit']
    option, not_needed = pick(options, title)
    return option


def pick_difficulty():
    title = "Difficulty"
    diff_options = ['Easy', 'Medium', 'Hard']
    diff_option, not_needed2 = pick(diff_options, title)
    return diff_option