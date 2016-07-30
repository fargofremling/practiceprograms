# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 
# and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers_to_add = []

def sum_of_multiples():

    for number in xrange (0, 1000):

        if number % 3 == 0 or number % 5 == 0:
            numbers_to_add.append(number)
            number += 1
        
        else:
            number += 1

    return numbers_to_add
    

sum_of_multiples()

def add(x, y):
    return x + y

sum = reduce(add, numbers_to_add)

print sum