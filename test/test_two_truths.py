from src.two_truths import display_options, is_correct_guess


def test_game_start_displays_three_options():
    options = { "1": True, "2": True, "option3": False }

    assert display_options(options) == options.keys()


def test_user_makes_incorrect_guess():
    guess = 1
    options = { "option0": True, "option1": True, "option2": False }

    assert is_correct_guess(guess, options) == False

def test_user_makes_correct_guess():
    guess = 2
    options = { "option0": True, "option1": True, "option2": False }

    assert is_correct_guess(guess, options) == True