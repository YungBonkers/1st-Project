import typer

#TYPE THE WORDS WITHIN 10 SECONDS

print("Type the words and hit enter within " 
      "the time limit! You have 10 seconds!")

num_words_per_round = [1, 2, 3]  # Custom number of words for each round
num_rounds = 3
difficulties = ["easy", "medium", "hard"]
total_rounds_won = 0

for difficulty in difficulties:
    print(f"Starting {difficulty} rounds...")

# Call rounds_won to play the game and track the number of rounds won
    rounds_won_count = typer.rounds_won(num_rounds,
                                    num_words_per_round, difficulty)
    total_rounds_won += rounds_won_count
    if rounds_won_count == 1:
        print("You won 1 " + difficulty + " round!")
    else:
        print(f"You won {rounds_won_count} {difficulty} rounds!")

    print("Thanks for playing.")

if total_rounds_won == 1:
    print("You won 1 round across all difficulties!")
else:
    print(f"You won a total of {total_rounds_won} across all difficulties!")
print("Game Over. Thanks for playing.")
