# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Python program to check if the input number is prime or not
num = 13195

primes = [2]

# prime numbers are greater than 1
for y in xrange(num):
    if y % 2 != 0:
        if (num % y) == 0:
            if (y % x for x in primes) != 0:
                primes.append(x)
            else:
                continue
        else:
            continue
    else:
        continue

print primes

#         if (num % i) == 0: