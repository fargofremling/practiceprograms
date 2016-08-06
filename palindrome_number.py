# A palindromic number reads the same both ways. The largest palindrome made from the 
# product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome():

   while True:
        user_input = raw_input("What word would you like to test? ")

        palindrome_test = user_input.lower()

        reverse = palindrome_test[::-1]

        if palindrome_test == reverse:
            isPalindrome = True

        else:
            isPalindrome = False

        if isPalindrome:
            print "Well, would you look at that;", user_input, "is a palindrome! \n"
        else:
            print "Sorry, Charlie,", user_input, "is not a palindrome. \n"

        play_again = raw_input("Would you like to test another word? Y or N \n")
    
        if play_again in ["y", "Y", "yes", "YES"]:
            continue
        
        else:
            print "Ciao!"
            break

palindrome()