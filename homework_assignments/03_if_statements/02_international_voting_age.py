# Problem Statement
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.


# List of countries and their voting ages:

countries = [
    ("Peturksbouipo", 16),
    ("Pakistan", 18),
    ("Stanlau", 25),
    ("Mayengua", 48),
    ("Zanvoria", 18),
    ("Lumeria", 21),
    ("Drakonia", 35),
    ("Eldoria", 40),
    ("Vortania", 20),
    ("Nexora", 30),
    ("America (USA)", 18),
    ("Europe", 18),
    ("South Korea", 18)
]
 
age = int(input("How old are you? ")) 

# check the condition using for loop:
for country_name, voting_age in countries:
     if age >= voting_age:
         print(f"You can vote in {country_name} where the voting age is {voting_age}.")
     else:
         print(f"You cannot vote in {country_name} where the voting age is {voting_age}.")

# output:
# How old are you? 20
# You can vote in Peturksbouipo where the voting age is 16.
# You can vote in Pakistan where the voting age is 18.     
# You cannot vote in Stanlau where the voting age is 25.   
# You cannot vote in Mayengua where the voting age is 48.  
# You can vote in Zanvoria where the voting age is 18.     
# You cannot vote in Lumeria where the voting age is 21.   
# You cannot vote in Drakonia where the voting age is 35.  
# You cannot vote in Eldoria where the voting age is 40.   
# You can vote in Vortania where the voting age is 20.     
# You cannot vote in Nexora where the voting age is 30.    
# You can vote in America (USA) where the voting age is 18.
# You can vote in Europe where the voting age is 18.       
# You can vote in South Korea where the voting age is 18.  




