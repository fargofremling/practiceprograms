# A palindromic number reads the same both ways.

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome():

    a = True
    
    product_number = 0
    
    y = 997

    x = 999

    while True:
        
           
        product = x * y
            
        product_string = str(product) 
            
        reverse = product_string[::-1]
        
        print y, x, product
    
        if product_string == reverse:
            
            print product_string
                
            return False
            
        elif product_number % 2 != 0:
            y -= 2
            x += 1
            product_number += 1
            
        else:
            x -= 2
            y += 1
            product_number += 1

palindrome()