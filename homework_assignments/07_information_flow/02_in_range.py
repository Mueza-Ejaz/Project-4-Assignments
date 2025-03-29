# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """
    

def in_range(n, low, high):
    return low <= n <= high   # Check if n is between low and high

print(in_range(5, 1, 10))  # True 
print(in_range(1, 1, 10))  # True 
print(in_range(0, 1, 10))  # False 




