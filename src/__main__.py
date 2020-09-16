import sys
from src.two_truths import play_game

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
        play_game()


if __name__ == '__main__':
    main()