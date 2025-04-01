# Mars Weight Solution:
# There are three key stages to solving this problem:

# Getting the Earthling's weight from them, which we need the input function for.

# Converting the Earthing's weight from a string to a number so we can do math with it. We use the float function to do this, since the weight isn't necessarily a whole number

# Calculating the weight on Mars, which we do by multiplying the Earth weight by 0.378. To make the program easy to read, we store this number in a constant called MARS_MULTIPLE.

#================================================================================================

# constant variable:
MARS_MULTIPLE = 0.378

def main():
    earth_weight = float(input('Enter a weight on Earth: '))
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    print(f"The equivalent weight on Mars: {rounded_mars_weight} \n") 

main()

# output:

# Enter a weight on Earth: 78
# The equivalent weight on Mars: 29.48 

#==========================================================================

# Planetary Weights Solution:
# There are two key parts to this solution:

# Everything from the first part of the problem: getting a user's input, converting it to a float to do the calculation, and covering it to a string to print it out.

# Using if statements to check which gravitational constant to use based on the user's input.

# constant gravity of planets:
MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ").capitalize()

    if planet_name == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet_name == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet_name == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet_name == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet_name == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet_name == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY  

    # calculate planets weight:
    planet_weight = earth_weight * gravity_constant
    rounded_planet_weight = round(planet_weight, 2)    

    print(f"The equivalent weight on {planet_name} : {rounded_planet_weight} \n")

main()    

# output:

# Enter a weight on Earth: 78
# Enter a planet: venus
# The equivalent weight on Venus : 69.34 
    




