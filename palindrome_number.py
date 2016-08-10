# A palindromic number reads the same both ways.

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome():

    a = True
    
    product_number = 0
    
    y = 999

    x = 999

    while a is True:
        
           
        product = x * y
            
        product_string = str(product) 
            
        reverse = product_string[::-1]
        print y, x, product
    
        if product_string == reverse:
                
            print y
            
            print x
            
            print product_string
                
            return a is False
            
        elif product_number % 2 != 0:
            y -= 1
            print y
            product_number += 1
            print product_number
            # return a is True
            
        else:
            x -= 1
            print x
            product_number += 1
            print product_number
            # return a is True

palindrome()