# Index Game Solution:

fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Accessing Elements:
def access_elements(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

# Modifying Elements: 
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."   
    

# Slicing the List:   
def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."
    

# Game Interaction:
def index_game():
    lst = [1, 2, 3, 4, 5]
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_elements(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()        

# output1:

# Current list: [1, 2, 3, 4, 5]
# Choose an operation: access, modify, slice
# Enter operation: access
# Enter index to access: 1
# 2

# output2:

# Current list: [1, 2, 3, 4, 5]
# Choose an operation: access, modify, slice
# Enter operation: modify
# Enter index to modify: 3
# Enter new value: 9
# [1, 2, 3, '9', 5]

# output3:

# Current list: [1, 2, 3, 4, 5]
# Choose an operation: access, modify, slice
# Enter operation: slice
# Enter start index: 0
# Enter end index: 3
# [1, 2, 3]

#===========================================================================

def main():
    # fruits list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# 1- Print the length of the list.
    print(len(fruit_list))

# 2- Add 'mango' at the end of the list. 
    fruit_list.append('mango')

# 3- Print the updated list.
    print(fruit_list)   

main() 

# output1 : 5 
# output2: ['apple', 'banana', 'orange', 'grape', 'pineapple', 'mango']








