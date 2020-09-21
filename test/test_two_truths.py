from src.two_truths import display_options, is_correct_guess, parse_user_selection


def test_options_displayed_to_user_from_game_input():
    options = { "1": True, "2": True, "option3": False }

    assert display_options(options) == options.keys()


def test_user_makes_incorrect_guess():
    guess = "my truth 1"
    options = { "my truth 1": True, "my truth 2": True, "my lie": False }

    assert is_correct_guess(guess, options) == False

def test_user_makes_correct_guess():
    guess = "my lie"
    options = { "option0": True, "option1": True, "my lie": False }

    assert is_correct_guess(guess, options) == True

def test_parse_user_selction_as_guess():
    user_selection = "3"
    options = { "option0": True, "option1": True, "my lie": False }
    guess = "my lie"

    assert parse_user_selection(user_selection, options) == guess

# TODO: add user_input validation
