def get_player_options(options):
    return options.keys()


def is_correct_guess(guess, options):
    return options[guess] == False


def parse_player_selection_as_guess(player_selection, player_options):
    options_index = player_selection - 1
    guess = list(player_options)[options_index]

    return guess

