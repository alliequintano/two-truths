from src.two_truths import get_player_options, is_correct_guess, parse_player_selection_as_guess


def test_get_player_options():
    options = { "1": True, "2": True, "option3": False }

    assert get_player_options(options) == options.keys()


def test_player_makes_incorrect_guess():
    guess = "my truth 1"
    options = { "my truth 1": True, "my truth 2": True, "my lie": False }

    assert is_correct_guess(guess, options) == False

def test_player_makes_correct_guess():
    guess = "my lie"
    options = { "option0": True, "option1": True, "my lie": False }

    assert is_correct_guess(guess, options) == True

def test_parse_player_selction_as_guess():
    player_selection = 3
    player_options = ("option0", "option1", "my lie")
    guess = "my lie"

    assert parse_player_selection_as_guess(player_selection, player_options) == guess
