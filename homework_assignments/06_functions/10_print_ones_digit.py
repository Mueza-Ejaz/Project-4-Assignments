# Problem Statement:
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2



def print_ones_digit(num):
    # divide by 10 to get the ones_digit
    ones_digit = num % 10

    print(f"The ones digit is {ones_digit}")

def main():
    user = int(input("Enter a number: "))
    print_ones_digit(user)

main()    

# output1:
# Enter a number: 42 
# The ones digit is 2

# output2:
# Enter a number: 147
# The ones digit is 7


# output3:
# Enter a number: 45897
# The ones digit is 7








