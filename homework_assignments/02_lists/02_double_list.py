# Problem Statement:
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

#------------------------------------------------------------------
# numbers = [2, 4, 3, 5]
# for num in numbers:
#     print(f"{2 * num}]") 

#-------------------------------------------------------------

# final solution:
numbers = [2, 4, 3, 5]

double_numbers = [num * 2 for num in numbers]  

print(f"Doubled list: {double_numbers}")


# output: Doubled list: [4, 8, 6, 10]






