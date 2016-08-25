# Problem #10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


n = int(raw_input("What prime number would you like to find?\n> "))

primes = []

for p in range(2, n+1):

    for x in range(2, p):
    
         if p % x == 0:
             break
    else:
        print p
        primes.append(p)
            
print primes
         
def add(x, y):
    return x + y

sum = reduce(add, primes)

print sum