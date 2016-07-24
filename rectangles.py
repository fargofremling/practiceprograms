# Challenge #276 [Easy] Rectangles
# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
# Given a word, a width and a length, you must print a rectangle with the word
# of the given dimensions.

# The input is a string word, a width and a height

def get_input():
    string = raw_input("What word would you like to put into a rectangel? \n> ").upper()
    
    split = list(string)
    
    print split[0], " ", split[1], " ", split[2], " ", split[3], " "
    print split[1], "         ", split[2]
    print split[2], "         ",split[1]
    print split[3], " ", split[2], " ", split[1], " ", split[0], " "

get_input()