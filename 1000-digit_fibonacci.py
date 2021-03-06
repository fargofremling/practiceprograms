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

print ("The Fibonacci Sequence is a series of numbers in which each term in the sequence"
" (Fibonacci number) is the sum of the two preceding numbers.")

print "Let's figure out what term of the Fibonacci sequence contains 1000 digits?"

# t = raw_input("> ")

fib_nums = []

def the_sequence():

    term = 0
    
    len_f = "0"
    # establishes first term in the sequence
    f = 0
    print f
    
    # establishes second term in the sequence
    g = 1
    
    while len(len_f) < 1001:
    
        if term % 2:
            f = f + g    
            print f
            len_f = str(f)
            if len_f == 1000:
                print "DONE"
                print "Answer:", len(fib_nums)
                return
                
            fib_nums.append(f)
            term += 1
            
        else:
            g = g + f
            print g
            len_g = str(f)
            if len(len_g) == 1000:
                print "DONE"
                print "Answer:", len(fib_nums)
                return
                
            fib_nums.append(g)
            term += 1

the_sequence()

# Answer: 4782
