def display_options(options):
    return options.keys()


def is_correct_guess(guess, options):
    return options[guess] == False


def parse_user_selection(user_selection, options):
    options_index = int(user_selection) - 1
    parsed_selection = list(options.keys())[options_index]

    return parsed_selection
