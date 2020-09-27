from src.game_logic import get_player_options, is_correct_guess, is_valid_selection, parse_player_input_as_guess


def play_two_truths(options):
    while True:
        player_options = get_player_options(options)
        display_options(player_options)

        guess = get_player_guess(player_options, prompt='Please select a number: ')
        if is_correct_guess(guess, options):
            print('You are correct!')
            return
        else:
            print('Try again!')


def display_options(player_options):
    for number, option in enumerate(player_options):
        number += 1
        print(number, option, sep=' - ', end='\n')


def get_player_guess(player_options, prompt):
    while True:
        try:
            player_input_as_int = int(input(prompt))
        except ValueError:
            print('Sorry, I did not understand that.')
            continue

        if is_valid_selection(player_input_as_int, player_options):
            return parse_player_input_as_guess(player_input_as_int, player_options)
        else:
            print('Sorry, I did not understand that.')
            continue