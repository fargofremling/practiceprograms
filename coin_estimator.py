# Goal Create a program that allows the user to input the total weight of each type 
# of coin they have (pennies, nickels, dimes, and quarters), and then print out how 
# many of each type of wrapper they would need, how many coins they have, and the 
# estimated total value of all of their money.
# Weight of each coin and how many fit inside each type of wrapper.

# Subgoals
# Round all numbers printed out to the nearest whole number.
# Allow the user to select whether they want to submit the weight in either grams or pounds.

# Penny = 2.5g, 50 per roll, $0.50, total weight per roll: 125g
# Nickel = 5.0g, 40 per roll, $2.00, total weight per roll: 200g
# Dime = 2.268g, 50 per roll, $5.00, total weight per roll: 112.4g
# Quarter = 5.67g, 40 per roll, $10.00, total weight per roll: 226.8g

# 1oz = 28.35g

import math

# creates a dictionary
coin_weights = {'pennies': ' ', 'nickels': ' ', 'dimes': ' ', 'quarters': ' '}
    
def get_unit():
    
    print "Would you like to use grams or ounces as your weight unit?"

    weight_type = raw_input("> ").lower()
    
    if weight_type in ["gram", "grams", "gr.", "gr", "g"]:
        return "grams"
    
    elif weight_type in ["ounce", "ounces", "oz.", "oz", "o"]:
        return "ounces"
    
    else:
        print "That wasn't one of the options, so we'll go with grams.\n"
        return "grams"

def get_weights():
    
    user_input_weight_type = get_unit()
    
    print  "Please enter the total weight for each of the following coins."

    if user_input_weight_type is "grams":
    
        while True:
            coin_weights['pennies'] = int(raw_input("\nPennies:\n> "))
            coin_weights['nickels'] = int(raw_input("\nNickels:\n> "))
            coin_weights['dimes'] = int(raw_input("\nDimes:\n> "))
            coin_weights['quarters'] = int(raw_input("\nQuarters:\n> "))
            
            try:
                return coin_weights

            except ValueError:
                print "Ah, weight needs to be a NUMBER! Try again using numbers."

    elif user_input_weight_type is "ounces":
    
        while True:
            coin_weights['pennies'] = int(raw_input("\nPennies:\n> ")) * 28.35
            coin_weights['nickels'] = int(raw_input("\nNickels:\n> ")) * 28.35
            coin_weights['dimes'] = int(raw_input("\nDimes:\n> ")) * 28.35
            coin_weights['quarters'] = int(raw_input("\nQuarters:\n> ")) * 28.35
            
            try:
                return coin_weights

            except ValueError:
                print "Ah, weight needs to be a NUMBER! Enter one, please."

def number_wrappers():

    get_weights()

    number_of_pennies = coin_weights['pennies'] / 2.5
    penny_wrappers = math.ceil(coin_weights['pennies'] / 125)
    print "You have", number_of_pennies, "pennies and will need,", penny_wrappers, "penny wrappers.\n"
    
    number_of_nickels = coin_weights['nickels'] / 5.0
    nickel_wrappers = math.ceil(coin_weights['nickels'] / 200)
    print "You have", number_of_nickels, "nickles and will need,", nickel_wrappers, "nickel wrappers.\n"
    
    number_of_dimes = coin_weights['dimes'] / 2.268
    dime_wrappers = math.ceil(coin_weights['dimes'] / 112.4)
    print "You have", number_of_dimes, "dimes and will need,", dime_wrappers, "dime wrappers.\n"

    number_of_quarters = coin_weights['quarters'] / 5.67
    quarter_wrappers = math.ceil(coin_weights['quarters'] / 226.8)
    print "You have", number_of_quarters, "quarters and will need,", quarter_wrappers, "quarter wrappers.\n"

number_wrappers()
