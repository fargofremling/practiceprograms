# Challenge #276 [Easy] Rectangles
# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
# Given a word, a width and a length, you must print a rectangle with the word
# of the given dimensions.

# The input is a string word, a width and a height

def get_input():

    string = raw_input("What word would you like to put into a rectangel? \n> ").upper()
    
    split = list(string)
    
    letters = len(split)
    
    print " ".join([str(x) for x in split])
    
    X = 1
    Y = -2
    
    for i in xrange(letters - 2):
    
        A = split[X]
        B = split[Y]

        print A, (" " * ((letters * 2) - 5)), B
        X += 1
        Y -= 1
    
    print " ".join([str(x) for x in split])[::-1]
    
get_input()