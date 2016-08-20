# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def the_function():
    
    for a in range(1,1000):
    
        for b in range (1, 1000):
        
            for c in range (1, 999):
            
                if (a**2 + b**2 == c**2):
                    print "Condition met: ", a,"^2 + ", b,"^2 = ",c,"^2"
                    
                    if (a + b + c == 1000):
                        print "a =", a
                        print "b =", b
                        print "c =", c
                        print "Answer:", a * b * c
                        return

the_function()

# a = 200
# b = 375
# c = 425
# a*b*c = 31875000