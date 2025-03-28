# Problem Statement:
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

def ran_num():

    # Pick a random number between 1 and 99 
    secret_num = random.randint(1, 99)

    print("Guess the number between 1 and 99! \n")

    while True:
      guess = int(input("Enter your guess: "))

      if guess < secret_num:  
          print("Your guess is too low!")  
      elif guess > secret_num:  
          print("Your guess is too high!")  
      else:  
            print(f"Congratulations! The number was: {secret_num} ")  
            break

ran_num()

# output:

# Guess the number between 1 and 99! 

# Enter your guess: 20
# Your guess is too high!
# Enter your guess: 10   
# Your guess is too high!
# Enter your guess: 7    
# Congratulations! The number was: 7 







