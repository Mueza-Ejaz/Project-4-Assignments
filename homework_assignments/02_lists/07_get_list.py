# Problem Statement:
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def user_list():
    lst = []  # empty list to store values

    ele = input("Enter a value: ")  # Get an initial value
    while ele:  # While the user input isn't an empty value
        lst.append(ele) # Add elements to list
        ele = input("Enter a value: ")  

    print(f"Here's the list: {lst}")

user_list()

# output:
# Enter a value: Mango
# Enter a value: Orange
# Enter a value: Milk
# Enter a value: 
# Here's the list: ['Mango', 'Orange', 'Milk']




