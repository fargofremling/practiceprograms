# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?


big_number = []

print 2**1000

def add(x,y): 
    return x+y

answer = reduce(add, big_number)

print answer