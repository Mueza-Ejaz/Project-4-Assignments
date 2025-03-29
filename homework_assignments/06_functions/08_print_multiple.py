# Problem Statement:
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!


def print_multiple():
    message = input("Please type a message: ")
    repeat = int(input("Enter a number of times to repeat your message: "))

    for i in range(repeat):
        print(f" {i}: {message}" )

print_multiple()        

# output:

# Please type a message: Hi, Mueza
# Enter a number of times to repeat your message: 7
#  0: Hi, Mueza
#  1: Hi, Mueza
#  2: Hi, Mueza
#  3: Hi, Mueza
#  4: Hi, Mueza
#  5: Hi, Mueza
#  6: Hi, Mueza






