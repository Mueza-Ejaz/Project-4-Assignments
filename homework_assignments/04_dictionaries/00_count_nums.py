# Problem Statement:
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


# Create an empty dictionary to store numbers and their counts
count_dict = {}

while True:
    num = input("Enter a number (or press enter to stop): ")

    if num == "": # If user presses enter without a number, stop the loop
        break 

    num = int(num) # convert user input in integer

    if num in count_dict: # If number is already in dictionary, increase the count
     count_dict[num] += 1
    else: # If number is not in dictionary, add it with count 1
       count_dict[num] = 1 

# Print each number with its count
for number, count in count_dict.items():
    print(f"{number} appears {count} times.")       

# output:

# Enter a number (or press enter to stop): 3
# Enter a number (or press enter to stop): 5
# Enter a number (or press enter to stop): 5
# Enter a number (or press enter to stop): 3
# Enter a number (or press enter to stop): 7
# Enter a number (or press enter to stop): 9
# Enter a number (or press enter to stop): 9
# Enter a number (or press enter to stop): 
# 3 appears 2 times.
# 5 appears 2 times.
# 7 appears 1 times.
# 9 appears 2 times.







