import sys
from src.game_view import play_two_truths


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
        play_two_truths(options = {"MyTruth1": True, "MyLie": False, "MyTruth2": True})


if __name__ == '__main__':
    main()