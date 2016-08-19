# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# (a + b + c == 12) and (a**2 + b**2 == c**2)

def the_function():
    for a in range(1,1000):
    
        for b in range (1, 1000):
        
            for c in range (1, 999):
            
                if (a + b + c == 1000):
                    print "Yes"
                    print a
                    print b
                    print c
                
                    if (a**2 + b**2 == c**2):
                        print "YES"
                        print "Answer?"
                        print a
                        print b
                        print c
                        return

the_function()
