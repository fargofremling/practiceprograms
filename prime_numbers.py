# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,and 17 we can see that 
# the 7th prime is 17.
# 
# What is the 10,001st prime number?

# I want to get the number of terms of prime number the user wants to find.
# In order to solve the problem the term must be the 10,001st.
n = int(raw_input("What prime number would you like to find?\n> "))

# I think that I want to store the prime numbers in an array. That way I stop the loop 
# (whatever kind I end up using, once the array gets to the nth prime number.
primes = []

# I was originally uses a for loop to establish p, but I'm trying to get experiment with
# a while loop, so instead I have to establish the term before I need it. 

p = 1
while n != len(primes):
#     for p in range(2, n+1)

    for x in range(1, p):
        p += 1
        if p % x == 0:
            break
    else:
        primes.append(p)
        print p
        print primes
        p += 1
    
print 'Done'
# This does not find the nth prime number. It instead only goes up to the number
# entered in the raw input.

# 
# # By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,and 17 we can see that 
# # the 7th prime is 17.
# # 
# # What is the 10,001st prime number?
# 
# print "Works!"
# 
# n = int(raw_input("What prime number would you like to find?\n> "))
# 
# for p in range(2, n+1):
#     for x in range(2, p):
#         if p % x == 0:
#             break
#     else:
#         print p,
# print 'Done'
# # This does not find the nth prime number. It instead only goes up to the number
# # entered in the raw input.