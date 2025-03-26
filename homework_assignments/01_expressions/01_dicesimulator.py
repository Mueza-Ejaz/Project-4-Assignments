# Problem Statement:
# Simulate rolling two dice, three times. Prints the results of each die roll. This program 
# is used to show how variable scope works.


# for choose randomly numbers,sequences, and generate choices :
import random

# Dice roll function
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Dice 1 = {die1}, Dice 2 = {die2}")
    print(f"Total: {total}\n")

# # Calling function 3 times
for i in range(3):
    roll_dice()

# output:
# Dice 1 = 3, Dice 2 = 6
# Total: 9

# Dice 1 = 4, Dice 2 = 1
# Total: 5

# Dice 1 = 3, Dice 2 = 2
# Total: 5





