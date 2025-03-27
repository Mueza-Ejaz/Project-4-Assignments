# Problem Statement:
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    print(f"First Element: {lst[0]}")  # print the first element

# Take input from the user and create a list:
num = int(input("How many elements do you want to add? "))

lst = [input("Enter Element: ") for _ in range(num)]  # num ki values ko list me store kary ga   

get_first_element(lst)

print(f"Final List = {lst}")

# output1:
# How many elements do you want to add? 3
# Enter Element: Juice
# Enter Element: Mango
# Enter Element: Milk
# First Element: Juice

# output2:
# How many elements do you want to add? 4
# Enter Element: Mango
# Enter Element: Apple
# Enter Element: Milk
# Enter Element: Sugar
# First Element: Mango
# Final List = ['Mango', 'Apple', 'Milk', 'Sugar']





