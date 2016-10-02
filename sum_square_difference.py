# The sum of the squares of the first ten natural numbers is, 
# 1**2 + 2**2 + ... + 10**2 = 385
# 
# The square of the sum of the first ten natural numbers is, 
# (1 + 2 + ... + 10)**2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 - 385 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.


# first part, squares sum

# creates list to later be reduced()
squares=[]

# establishes x for 1 to 100
for x in range(101):
    
    # finds the square of x for 1 to 100
    y = x**2
    
    # adds the square to the squares list
    squares.append(y)

# creates the add method for use in the reduce method
def add(x,y): return x+y

squares_sum = reduce(add, squares)

print  squares_sum

# second part
sum = sum(range(101))

print sum

# third part
answer = sum**2 - squares_sum

print answer
