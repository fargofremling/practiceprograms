# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

evens = []

def the_sequence():
    
    # establishes first term in the sequence
    f = 0
    
    # establishes second term in the sequence
    g = 1
    
    while f < 4000000:
    
        if f % 2:
            f = f + g    
            if f % 2 == 0:
                evens.append(f)
            else:
                continue
        else:
            g = g + f
            if g % 2 == 0:
                evens.append(g)
            else:
                continue

the_sequence()

print evens

def add(x, y):
    return x + y

sum = reduce(add, evens)

print sum