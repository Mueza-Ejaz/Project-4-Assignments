# Problem Statement:
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    print(f"Last Element: {lst[-1]}")  # print the last element

# Take input from the user and create a list:
num = int(input("How many elements do you want to add? "))

lst = [input("Enter Element: ") for _ in range(num)]  # num ki values ko list me store kary ga   

get_last_element(lst)

print(f"Final List = {lst}")

# output:
# How many elements do you want to add? 3
# Enter Element: juice
# Enter Element: milk
# Enter Element: water
# Last Element: water
# Final List = ['juice', 'milk', 'water']





