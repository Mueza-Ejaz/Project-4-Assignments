# Problem Statement:
# In this program we show an example of using dictionaries to keep track of information in a phonebook.


# empty phonebook dictionary:
phonebook = {}

# input from user name and number:
while True:
    name = input("Name: ")

    if name == "":  # Stop if input empty
        break  

    phonebook[name] = input("Number: ") # store number
    print("\nPhonebook:")
    
    for name, number in phonebook.items():
     print(f"{name} -> {number}")

    # searching user number
while True:
    search_name = input("\nEnter name to lookup: ")
    if search_name == "":  
        break
    print(phonebook.get(search_name, "Name not found in phonebook"))

# output:

# Name: Mueza
# Number: 03242320220

# Phonebook:
# Mueza -> 03242320220
# Name: Ali
# Number: 03452844416

# Phonebook:
# Mueza -> 03242320220
# Ali -> 03452844416  
# Name: shahroz
# Number: 03241256589

# Phonebook:
# Mueza -> 03242320220
# Ali -> 03452844416
# shahroz -> 03241256589
# Name:

# Enter name to lookup: Mueza
# 03242320220







