# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,and 17 we can see that 
# the 7th prime is 17.
# 
# What is the 10,001st prime number?

print "Works!"

n = int(raw_input("What prime number would you like to find?\n> "))

for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print p,
print 'Done'