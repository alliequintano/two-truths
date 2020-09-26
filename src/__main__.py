import sys, json
from src.two_truths import get_player_options, is_correct_guess, parse_player_selection


def main():
    """Usage: two-truths [OPTIONS]

        TODO: describe how to play the game
        TODO: would be kind of cool to have game options for easy, medium, hard?

    Options:
      --help       Show this message

    """

    args = sys.argv[1:]
    for arg in args:
        if (arg == '--help'):
            print(main.__doc__)
            break
    else:
        with open('default.json') as json_file:
            game_data = json.loads(json_file)
            while True:
                for option in get_player_options(game_data):
                    print(option, sep=' - ', end='\n')
                guess = parse_player_selection(
                    input('select a number: '), get_player_options)

                if is_correct_guess(guess, game_data):
                    print('You are correct!')
                    break
                else:
                    print('Try again!')


if __name__ == '__main__':
    main()
