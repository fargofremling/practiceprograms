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

# 100g = 0.22lbs
import math

coin_weights = {'pennies': ' ', 'nickels': ' ', 'dimes': ' ', 'quarters': ' '}
    
def get_unit():

    print "Would you like to use grams or pounds as your weight unit?"
    weight_type = raw_input("> ").lower
#     if weight_type in [gram, grams, g]:
#         return grams
#     elif weight_type in [pound, pounds, lb, lbs]:
#         return pounds

def get_weights():

    print  "Please enter the total weight for each of the following coins."

    coin_weights['pennies'] = raw_input("\nPennies:\n> ")
    coin_weights['nickels'] = raw_input("\nNickels:\n> ")
    coin_weights['dimes'] = raw_input("\nDimes:\n> ")
    coin_weights['quarters'] = raw_input("\nQuarters:\n> ")
    
def number_wrappers():
   
    penny_wrappers = math.ceil(int(coin_weights['pennies']) / 125)
    print "You will need,", penny_wrappers, "penny wrappers.\n"
    
    nickel_wrappers = math.ceil(int(coin_weights['nickels']) / 200)
    print "You will need,", nickel_wrappers, "nickel wrappers.\n"
    
    dime_wrappers = math.ceil(int(coin_weights['dimes']) / 112.4)
    print "You will need,", dime_wrappers, "dime wrappers.\n"

    quarter_wrappers = math.ceil(int(coin_weights['quarters']) / 226.8)
    print "You will need,", quarter_wrappers, "quarter wrappers.\n"

def main():
    get_unit()
    get_weights()
    number_wrappers()
    
main()
