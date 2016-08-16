# A palindromic number reads the same both ways.

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import timeit

start = timeit.default_timer()

actual_palindromes = []

def palindrome():

    for y in xrange(100, 1000):
        
        for x in xrange(100,1000):
        
            if x >= y: 
                product = x * y
    
                product_string = str(product) 
    
                reverse = product_string[::-1]
    
                if product_string == reverse:
        
                    print y
        
                    print x
            
                    print product_string
            
                    actual_palindromes.append(product)
        
                    isPalindrome = True

                    print "isPalindrome"
        
                else:
                    isPalindrome = False

    actual_palindromes.sort()        

    print actual_palindromes

    print actual_palindromes[-1]

palindrome()

stop = timeit.default_timer()

print stop - start 

# 0.587522983551 - without x >= y

# 0.318891048431 - with x >= y