import sys
from src.two_truths import display_options, is_correct_guess


def main():
    """Usage: two-truths [OPTIONS]

        ¯\_(ツ)_/¯

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
            print(*display_options(options), sep='\n')
            if is_correct_guess(int(input('select a number: ')), options):
                print('You are correct!')
                break
            else:
                print('Try again!')


if __name__ == '__main__':
    main()