# GOAL
# Define a function that allows the user to find the value of the nth term in the
# sequence. To make sure you've written your function correctly, test the first 10 
# numbers of the sequence. Remember, the 0th term is 0 and the first and second term 
# are both 1.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def the_sequence():

    f = 0
    print f
    
    g = 1
    print g
    
    # while loop is required - does not work with for loops
    while g in range (0, 100):
    
        f = f + g    
        print f
    
        g = g + f
        print g

the_sequence()