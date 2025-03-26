# Problem Statement:
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.


# method 01:
# Useful constants to help make the math easier and cleaner!
# DAYS_PER_YEAR: int = 365
# HOURS_PER_DAY: int = 24
# MIN_PER_HOUR: int = 60
# SEC_PER_MIN: int = 60

# def main():
#     # We can get the number of seconds per year by multiplying the handy constants above!
#     print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()

# Constants
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60
WEEKS_PER_YEAR = 52
MONTHS_PER_YEAR = 12

def calculate_time():
    # input from user:
    years = int(input("Enter number of years:"))

    # Calculations
    total_days = years * DAYS_PER_YEAR
    total_weeks = years * WEEKS_PER_YEAR
    total_months = years * MONTHS_PER_YEAR
    total_hours = years * DAYS_PER_YEAR * HOURS_PER_DAY
    total_seconds = total_days * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Output
    print(f"\nIn {years} years:")
    print(f"- There are {total_months} months.")
    print(f"- There are {total_weeks} weeks.")
    print(f"- There are {total_days} days.")
    print(f"- There are {total_hours} hours.")
    print(f"- There are {total_seconds} seconds!\n")

calculate_time()   

# output:
# Enter number of years:4

# In 4 years:
# - There are 48 months.        
# - There are 208 weeks.        
# - There are 1460 days.        
# - There are 35040 hours.      
# - There are 126144000 seconds!





