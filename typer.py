import random
import time
import word_bank  
# Ensure word_bank.py is correctly implemented and in the same directory

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input(f"({seconds} seconds) {words}\n")
    stop = time.time()

    # Fail the round if a word is misspelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, difficulty):
    """Returns a random phrase containing the given number of
    words based on difficulty.""" 
    words = [get_random_word(difficulty) for _ in range(num_words)]
    return ' '.join(words)

def get_random_word(mode):
    """Returns a random word with a word length based on
    the given difficulty mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)

def rounds_won(num_rounds, num_words_per_round, difficulty):
    """Keeps track of how many rounds won."""
    rounds_won_count = 0  # Counter for rounds won

    for round in range(1, num_rounds + 1):
        num_words = num_words_per_round[round - 1]
        words_to_type = pick_random_words(num_words, difficulty)
        
        # Use play_round to prompt user input and check the round outcome
        if play_round(words_to_type, 10):
            rounds_won_count += 1  # Increment the rounds won counter
            print("You won this round!")
        else:
            print("Oops! You lost this round.")
            break  # Exit the loop if the user fails a round

    return rounds_won_count

def rounds_won_check(words, response):
    """Checks if the response matches the words."""
    return response == words