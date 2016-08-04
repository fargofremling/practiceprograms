# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Python program to check if the input number is prime or not

# take input from the user
num = 13195

primes = []

# prime numbers are greater than 1
for x in xrange(num):
    if x % 2 != 0:
        if (num % x) != 0:
            primes.append(x)
            x += 1
        else:
            x += 1
       # check for factors
       # for i in range(2,num):
#            if (num % i) == 0:
#                print num,"is not a prime number"
#                print i,"times",num//i,"is",num
#                break
    else:
       x += 1

print primes

#         if (num % i) == 0: