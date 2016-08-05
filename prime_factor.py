# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Python program to check if the input number is prime or not
num = 600851475143

primes = [2]

print num

# prime numbers are greater than 1
for y in xrange(2, num):

    if y % 2 != 0:
        print y
        
        if (num % y) == 0:
        
            not_prime = False
            
            for x in primes:
            
                if y % x == 0:
                
                    not_prime = True
                    break
                
                else:
                    not_prime = False
                    
            if not_prime == False:
                primes.append(y)
            
            else: 
                continue
        else:
            continue
    else:
        continue

print primes

