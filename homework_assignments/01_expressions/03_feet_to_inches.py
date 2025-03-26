# Problem Statement:
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


INCHES_IN_FOOT = 12  # 12 inches in 1 foot

def inches():
    feet = float(input("Enter number of feet: ")) 

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT  
    
    print(f"{feet} feet = {inches} inches.")

inches()   

# output:
# Enter number of feet: 4
# 4.0 feet = 48.0 inches.


