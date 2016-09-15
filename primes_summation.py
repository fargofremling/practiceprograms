# Problem #10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

import timeit
import math

start = timeit.default_timer()

n = int(raw_input("What prime number would you like to find?\n> "))

primes = [2,3]

for p in range(5, n+1, 2):
    if any(p % i == 0 for i in primes):
#     p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0 or p % 13 == 0:
        continue
    else:
        for x in range(2, int(math.sqrt(p)):
    
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

stop = timeit.default_timer()

print stop - start

# answer: 142913828922