# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

#--------------------------------------------------------------------------

# Milestone #1: Mars Weight

# Mars Weight=Earth Weight×0.378

# take input from user:
earth_weight = float(input("Enter your weight on Earth: "))

# calculate mars weight:
mars_weight = round(earth_weight * 0.378, 2)

print(f"The equivalent weight on Mars: {mars_weight}\n")

# output 1:

# Enter your weight on Earth: 45
# The equivalent weight on Mars: 17.01

#================================================================================

# Milestone #2: Adding in All Planets
# dictionary 
planets_gravity = {
    "Mercury": 37.6,
    "Venus": 88.9,  
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

# take input from user:
earth_weight = float(input("Enter a weight on Earth: "))
planet_name = input("Enter a planet: ").capitalize() # capital first letter 

# Calculate weight on the selected planet:
if planet_name in planets_gravity:
    planet_weight = round(earth_weight * (planets_gravity[planet_name] /100), 2)
    print(f"The equivalent weight on {planet_name}: {planet_weight:.2f}")
else:
    print("Invalid planet name!")

# output1:

# Enter a weight on Earth: 120
# Enter a planet: Mars
# The equivalent weight on Mars: 45.36

# output2:

# Enter a weight on Earth: 150
# Enter a planet: Jupiter
# The equivalent weight on Jupiter: 354.00








