import random

def high_low_game():
    score = 0   # initial score 0
    rounds = 5
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # for loop:
    for round_num in range(1, rounds + 1):
        user_number = random.randint(1, 100) # randomly generate number for user 
        computer_number = random.randint(1, 100) # randomly generate number  for computer 
        
        print(f"\nRound {round_num}")
        print(f"Your number is {user_number}")
        guess = input("Is your number higher or lower than the computer's? (higher/lower): ").lower()
        
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"Correct! The computer's number was {computer_number}")
            score += 5 # Add 5 only for correct answers
        else:
            print(f"Wrong! The computer's number was {computer_number}")
        
        print(f"Your score: {score}")
    
    # Game Over Message
    print("\n--------------------------------")
    print(f" Game Over! Your total score is: {score} out of {rounds * 5}")
    print("Thanks for playing! :) ")


high_low_game()


# output:

# Welcome to the High-Low Game!
# --------------------------------

# Round 1
# Your number is 84
# Is your number higher or lower than the computer's? (higher/lower): higher
# Wrong! The computer's number was 97
# Your score: 0

# Round 2
# Your number is 75
# Is your number higher or lower than the computer's? (higher/lower): lower
# Correct! The computer's number was 98
# Your score: 5

# Round 3
# Your number is 58
# Is your number higher or lower than the computer's? (higher/lower): lower
# Wrong! The computer's number was 22
# Your score: 5

# Round 4
# Your number is 71
# Is your number higher or lower than the computer's? (higher/lower): higher
# Correct! The computer's number was 29
# Your score: 10

# Round 5
# Your number is 4
# Is your number higher or lower than the computer's? (higher/lower): lower
# Correct! The computer's number was 72
# Your score: 15

# --------------------------------
#  Game Over! Your total score is: 15 out of 25
# Thanks for playing! :)



      