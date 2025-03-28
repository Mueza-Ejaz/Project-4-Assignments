# Problem Statement:
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5


# making a fruit dictionary 
fruit_prices = {

    "apple":5.00,
    "durian": 15.00,
    "jackfruit": 10.00,
    "kiwi": 7.50,
    "rambutan": 8.00,
    "mango": 12.00

}

# variable of total cost:
total_cost = 0

print("\nYour Order Summary:\n")

# get the quantity of fruits from user:
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many ({fruit}) do you want?: ")) 

    item_total = quantity * price  # Ek fruit ki total cost

    total_cost += item_total  # update total cost
    print(f"{fruit}: {quantity} × ${price:.2f} = ${item_total:.2f}")  

# total fine price:
print(f"\nTotal Cost: ${total_cost:.2f}")

# output:

# Your Order Summary:

# How many (apple) do you want?: 2
# apple: 2 × $5.00 = $10.00       
# How many (durian) do you want?: 3
# durian: 3 × $15.00 = $45.00        
# How many (jackfruit) do you want?: 5
# jackfruit: 5 × $10.00 = $50.00
# How many (kiwi) do you want?: 4
# kiwi: 4 × $7.50 = $30.00
# How many (rambutan) do you want?: 7
# rambutan: 7 × $8.00 = $56.00   
# How many (mango) do you want?: 5
# mango: 5 × $12.00 = $60.00

# Total Cost: $251.00




