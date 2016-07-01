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

term = 0

def the_sequence():

    global term

    # establishes first term in the sequence
    f = 0
    print f
    
    # establishes second term in the sequence
    g = 1
    
    while term < (int(t) - 1):
    
        if term % 2:
            f = f + g    
            print f
            term += 1
        else:
            g = g + f
            print g
            term += 1

the_sequence()