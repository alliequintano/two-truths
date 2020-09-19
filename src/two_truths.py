def display_options(options):
    return(options.keys())


def is_correct_guess(guess, options):
    return(list(options.values())[guess] == False)