import sys
from src.two_truths import display_options, is_correct_guess, parse_user_selection


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
            for number, option in enumerate(display_options(options)):
                number += 1
                print(number, option, sep=' - ', end='\n')
            guess = parse_user_selection(input('select a number: '), options)

            if is_correct_guess(guess, options):
                print('You are correct!')
                break
            else:
                print('Try again!')


if __name__ == '__main__':
    main()