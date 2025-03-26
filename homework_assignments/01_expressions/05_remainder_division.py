# Problem Statement:
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2



def division():
    num1 = int(input("Please enter an integer to be divided: ")) # Dividend
    num2 = int(input("Please enter an integer to divide by: "))  # Divisor

    quotient = num1 // num2  # Integer division (quotient)
    remainder = num1 % num2  # Modulus (remainder)

    print(f"{num1} // {num2} = {quotient}")
    print(f"{num1} % {num2}= {remainder}")
    print(f"The result of this division is {quotient} with a remainder of {remainder}\n")

division()

# output:
# Please enter an integer to be divided: 9
# Please enter an integer to divide by: 3
# 9 // 3 = 3
# 9 % 3= 0
# The result of this division is 3 with a remainder of 0






