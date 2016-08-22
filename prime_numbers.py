# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,and 17 we can see that 
# the 7th prime is 17.
# 
# What is the 10,001st prime number?

primes = []

n = int(raw_input("What prime number would you like to find?\n> "))

p = 2
    
while len(primes) != n:
    
    for x in range(2, p):
        
        if p % x == 0:
            p += 1
            break
            
    else:
        primes.append(p)
        p += 1

print 'Done'
print primes[-1]

# Answer: 104743