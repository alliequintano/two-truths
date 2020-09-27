from src.game_logic import get_player_options, is_correct_guess, parse_player_input_as_guess, is_valid_selection


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


def test_parse_player_input_as_guess():
    player_input_as_int = 3
    player_options = ("option0", "option1", "my lie")
    guess = "my lie"

    assert parse_player_input_as_guess(player_input_as_int, player_options) == guess


def test_is_valid_selection():
    assert is_valid_selection(player_input_as_int=1, player_options=("option0", "option1", "my lie")) == True


def test_is_invalid_selection():
    assert is_valid_selection(player_input_as_int=0, player_options=("option0", "option1", "my lie")) == False