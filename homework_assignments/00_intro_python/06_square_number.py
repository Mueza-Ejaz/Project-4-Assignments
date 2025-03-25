# Problem Statement:
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


def squr_num():
    num = float(input("Type a number to see its square: "))

    print(f"{num} squared is: {num * num}")


squr_num()

#output1:
# Type a number to see its square: 5
# 5.0 squared is: 25.0

#output2:
# Type a number to see its square: 4
# 4.0 squared is: 16.0