# The Fibonacci sequence is defined by the recurrence relation:
# 
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

print ("The Fibonacci Sequence is a series of numbers in which each term in the sequence"
" (Fibonacci number) is the sum of the two preceding numbers.")

print "To what term would you like to see the sequence calculated?"

t = raw_input("> ")

fib_nums = []

def the_sequence():

    term = 0
    
    # establishes first term in the sequence
    f = 0
    print f
    
    # establishes second term in the sequence
    g = 1
    
    while term < (int(t) - 1):
    
        if term % 2:
            f = f + g    
            print f
            fib_nums.append(term)
            term += 1
            
        else:
            g = g + f
            print g
            fib_nums.append(term)
            term += 1
        
        for str(x) in fib_nums:
            if len(x) == 1000:
                print x
                return
            
the_sequence()


