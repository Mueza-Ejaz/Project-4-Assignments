# Problem Statement:
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1- Prompt the user to enter the first number.

# 2- Read the input and convert it to an integer.

# 3- Prompt the user to enter the second number.

# 4- Read the input and convert it to an integer.

# 5- Calculate the sum of the two numbers.

# 6- Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.


def main():
    print("This program adds two numbers.")

# input 1:
    user1 = input("Enter first number: ")
    num1 = int(user1)

#input 2:
    user2  = input("Enter second number: ")
    num2 = int(user2)

# add input 1 and input 2:
    total = num1 + num2

    print(f"The total is {total} .") # output: The total is 15 .


# It makes sure the code runs only when you run the file, not when you import it.
if __name__ == '__main__': # Entry Point Check
    main()