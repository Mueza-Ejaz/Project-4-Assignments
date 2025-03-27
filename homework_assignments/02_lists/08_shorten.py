# Problem Statement:
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# conclusion:
# Humey list ko chotta karna hy agr uski elements ki lenght MAX_LENGTH sy barri hoo jo humny by-default uski value set ki hogi .agr usk baraber hy to phir aisi hii list ko print karna hy. 

# limits of maximum elements in empty list
MAX_LENGTH = 4

def shorten(list):
    print(f"Maximum Lenght of Elements is {MAX_LENGTH}\n")
    num = int(input("How many elements do you want to add? ")) 

    list = [input("Enter Element: ") for _ in range(num)]  # List me elements add karo

    while len(list) > MAX_LENGTH: # lenght of list is greater than MAX_LENGTH

        removed = list.pop() # remove last element
        print(f"Removing: {removed}")

    print(f"\nFinal list: {list}")  # After removing last elements print final list  
 
shorten(list)

# output:
# Maximum Lenght of Elements is 4

# How many elements do you want to add? 7
# Enter Element: Mango
# Enter Element: Sugar
# Enter Element: Milk
# Enter Element: Water
# Enter Element: Chocolate
# Enter Element: Dates
# Enter Element: Elmonds
# Removing: Elmonds
# Removing: Dates
# Removing: Chocolate

# Final list: ['Mango', 'Sugar', 'Milk', 'Water']






