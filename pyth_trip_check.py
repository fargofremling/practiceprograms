
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.
# Extra Credit
# If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.
# Loop the program so the user can use it more than once without having to restart the program.
a = 0
b = 0
c = 0

def triangle_sides():
    global a, b, c
    side1 = int(raw_input("What is the shortest side of the triangle you want to check?\n"))
    side2 = int(raw_input("The middle side?\n"))
    side3 = int(raw_input("And the longest side?\n"))
    
    list = [side1, side2, side3]
    print sorted(list)
    print list
    return a, b, c

def c_odd():
    global a, b, c
    if c % 2 == 0:
        return False
    elif (a % 2 == 0) and (b % 2 == 0):
        return False
    elif (a % 2 == 1) and (b % 2 == 1):
        return False
    elif (a % 3 == 0) and (b % 3 == 0):
        return False
    elif (a % 3 != 0) and (b % 3 != 0):
        return False
    elif (a % 4 == 0) and (b % 4 == 0):
        return False
    elif (a % 4 != 0) and (b % 4 != 0):
        return False
    elif (a % 5 == 0) and (b % 5 == 0):
        return False
    elif (a % 5 != 0) and (b % 5 != 0) and (c % 5 != 0):
        return False
    elif (c + a) % 2 != (c - a) % 2:
        return False
    elif (c + a) % 2 != (c - a) % 2:
        return False
    else:
        return True

def main_function():
    while True:
        triangle_sides()
        pyth_trip = c_odd()

        if pyth_trip == True:
            print "Looks like you discovered a Pythagorean Triple!"
        elif pyth_trip == False:
            print "Sorry, Charlie. That is not a Pythagorean Triple."

        check_again = raw_input("Do you want to check another triangle?\n").lower()

        if check_again in ["yes", "y"]:
            continue
        else:
            print "Thanks for tri-ing this program!"
            break

main_function()


# At most one of a, b, c is a square.
# The area of a Pythagorean triangle cannot be the square[9]:p. 17 or twice the square[9]:p. 21 of a natural number.
# Exactly one of a, b is odd; c is odd.
# Exactly one of a, b is divisible by 3.
# Exactly one of a, b is divisible by 4.
# Exactly one of a, b, c is divisible by 5.
# The largest number that always divides abc is 60.
# All prime factors of c are primes of the form 4n + 1. Therefore c is of the form 4n + 1.


# More rules:
# An interesting fact: a Pythagorean Triple always consists of: all even numbers, or two odd numbers and an even number.
# A Pythagorean Triple can never be made up of all odd numbers or two even numbers and one odd number. This is true because:

# The square of an odd number is an odd number and the square of an even number is an even number.

# It is easy to construct sets of Pythagorean Triples.

# When m and n are any two positive integers (m < n):

# a = n**2 - m**2
# b = 2nm
# c = n**2 + m**2
