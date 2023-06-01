# Name: Lucas Hochberg
# Date: 5/2/23
# Description: Randomly prints a group of menu items, 1 from each column, based on the lists
# Bugs: Getting the food to print instead of restarting the code/Having to add extra number lists for prices/Setting the prices to a certain item
# Challenges: There is a cost for every item/There are no repeats in the items
# Sources: Ms. Marciano, Henry Santangelo

import random # Loads the random module

column1 = ["local", "roasted", "grilled", "garlic mashed", "oven dried", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby", "teriyaki glazed", "steamed"] # Creates a list of items for column 1
price1 = [1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 5] # Creates a list of prices for column 1
column2 = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "basmati rice", "rainbow carrots", "fingerling potatoes", "three color squash", "potatoes", "eggplant", "drumstick", "short rib", "duck breast", "eye round of beef", "baguette"] # Creates a list of items for column 2
price2 = [3, 10, 12, 4, 3, 2, 1, 1, 2, 3, 4, 12, 11, 10, 5] # Creates a list of prices for column 2
column3 = ["with fennel", "gratin", "bengali style", "with peas", "pizza", "with balsamico", "with garlic and olive oil", "with pigeon peas", "with minted yogurt", "soup", "chutney", "salad", "with tropical fruit salsa", "over sticky rice", "au jus"] # Creates a list of items for column 3
price3 = [1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 5] # Creates a list of prices for column 3
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Creates a list of numbers

while True: # Creates a loop
    mode = input("what would you like to do? create/exit: ") # Asks the user this message
    if mode.lower() == "create": # If user selects create
        items = input("How many menu items would you like: ") # Asks the user this message
        try: # Executes the code with no errors
            items = int(items) # Indicates the items integer
            used = [] # Creates the used list
            for i in range(items): # Generates a sequence of numbers within items
                while True: # Creates a loop
                    price = 0 # Allows the price to be set to a number
                    col1 = random.choice(column1) # Makes a random choice for column 1
                    col2 = random.choice(column2) # Makes a random choice for column 2
                    col3 = random.choice(column3) # Makes a random choice for column 3
                    price += price1[column1.index(col1)] # Makes the price set to its corresponding price in column 1
                    price += price2[column2.index(col2)] # Makes the price set to its corresponding price in column 2
                    price += price3[column3.index(col3)] # Makes the price set to its corresponding price in column 3

                    meal = f"{col1} {col2} {col3}" # Allows meal to access all items
                    if not meal in used: # If the item is not used
                        print(meal, ": $", price) # Prints this message
                        used.append(meal) # Adds used items to meals
                        break # Ends
        except ValueError: # Allows an exception for values
            print("Input must be an integer") # Prints this message
    if mode.lower() == "exit": # If user enters exit
        break # Ends