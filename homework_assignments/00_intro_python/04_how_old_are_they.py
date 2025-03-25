# Problem Statement:
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.
#---------------------------------------------------------------------

def ages():
    anton = 21 
    beth  = 6 + anton  
    chen  = 20 + beth  
    drew  = chen + anton  
    ethan = chen 

   # Print all the ages:

    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

ages() 

#output: 
# Anton is 21
# Beth is 27
# Chen is 47
# Drew is 68
# Ethan is 47