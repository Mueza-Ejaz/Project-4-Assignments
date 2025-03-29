# Problem Statement:
# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!




def count_even(list):
    list = []  # Empty list
    even_numbers = [] # store even numbers

    while True:
        user_input = input("Enter an integer or (press enter to stop): ")
        if user_input == "":
            break

        num = int(user_input)  # convert user_input numbers in integer
        list.append(num) # add the numbers in empty list

        if num % 2 == 0:
            even_numbers.append(num)
        
    # count the even numbers:
    even_count = len(even_numbers)

    print(f"Even Numbers: {even_numbers}")
    print(f"Total Even Numbers: {even_count}")

count_even(list)    

# output:

# Enter an integer or (press enter to stop): 4
# Enter an integer or (press enter to stop): 8
# Enter an integer or (press enter to stop): 5
# Enter an integer or (press enter to stop): 9
# Enter an integer or (press enter to stop): 7
# Enter an integer or (press enter to stop): 10
# Enter an integer or (press enter to stop): 2
# Enter an integer or (press enter to stop): 
# Even Numbers: [4, 8, 10, 2]
# Total Even Numbers: 4  






