# A palindromic number reads the same both ways.

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome():

    for y in range(999, 99, -1):
    
        for x in xrange(999, 9, -1):
            
            product = x * y
            
            product_string = str(product) 
            
            reverse = product_string[::-1]
         
            if product_string == reverse:
                
                print y
                
                print x
                
                print product_string
                
                break
            
            else:
                continue
        break

palindrome()