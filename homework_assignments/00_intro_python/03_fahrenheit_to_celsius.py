# Problem Statement:
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C\
#---------------------------------------------------------------


user_temp = float(input("Enter temperature in Fahrenheit:"))
degrees_celsius = (user_temp - 32) * 5.0/9.0

print(f"Temperature: {user_temp}°F = {degrees_celsius}°C")

# output1: Enter temperature in Fahrenheit:76
# Temperature: 76.0°F = 24.444444444444443°C

# output2: Enter temperature in Fahrenheit:45
# Temperature: 45.0°F = 7.222222222222222°C 