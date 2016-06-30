# GOAL
# Define a function that allows the user to find the value of the nth term in the
# sequence. To make sure you've written your function correctly, test the first 10 
# numbers of the sequence. Remember, the 0th term is 0 and the first and second term 
# are both 1.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

print ("The Fibonacci Sequence is a series of numbers in which each term in the sequence"
" (Fibonacci number) is the sum of the two preceding numbers.")

print "To what term would you like to see the sequence calculated?"

t = raw_input("> ")

def the_sequence():

    f = 0
    print f
    
    g = 1
    print g
    
    for _ in range(int(t) - 2):
    # while loop is required - does not work with for loop
#     while g in range (1, int(t) - 2):
#     while f < (int(t) - 2):
    
        f = f + g    
        print f
    
        g = g + f
        print g

the_sequence()