# Problem Statement:
# Simulate rolling two dice, and prints results of each roll as well as the total.


import random


def rolling_dice():

    # Roll die
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
  
  # Print out the results
    print(f"Dice have 6 sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


rolling_dice()

# output:
# Dice have 6 sides each.
# First die: 4
# Second die: 5
# Total of two dice: 9






