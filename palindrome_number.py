# A palindromic number reads the same both ways.

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

actual_palindromes = []

def palindrome():

    for y in xrange(100, 1000):
        
        for x in xrange(100,1000):
        
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