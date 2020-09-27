import sys
from src.two_truths import get_player_options, is_correct_guess, parse_player_selection_as_guess


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
        options = {"MyTruth1": True, "MyLie": False, "MyTruth2": True}
        while True:
            player_options = get_player_options(options)

            for number, option in enumerate(player_options):
                number += 1
                print(number, option, sep=' - ', end='\n')

            while True:
                try:
                    player_selection = int(input('Please select a number: '))
                except ValueError:
                    print('Sorry, I did not understand that.')
                    continue
                if player_selection > len(player_options) or player_selection <= 0:
                    print('Sorry, I did not understand that.')
                    continue
                else:
                    guess = parse_player_selection_as_guess(player_selection, player_options)
                    if is_correct_guess(guess, options):
                        print('You are correct!')
                        break
                    else:
                        print('Try again!')
            break


if __name__ == '__main__':
    main()