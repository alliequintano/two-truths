def get_player_options(options):
    return options.keys()


def is_correct_guess(guess, options):
    return options[guess] == False


def parse_player_input_as_guess(player_input_as_int, player_options):
    options_index = player_input_as_int - 1
    guess = list(player_options)[options_index]

    return guess

def is_valid_selection(player_input_as_int, player_options):
    return player_input_as_int <= len(player_options) and player_input_as_int > 0
