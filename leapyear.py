# To determine whether a year is a leap year, follow these steps:
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).

def leap_year_check():
    
    while True:
        try:
            year = int(raw_input("What year would you like to check? \n> "))
    
            if year % 4 != 0:
                print "Nope, it's not a leap year."
                break
                
            elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
                print "Nope, it's not a leap year."
                break
            
            else:
                print "Yep, it's a leap year. Hooray for an extra day!"
                break
                
        except ValueError:
            print "A year is supposed to be a number. Please enter a number. \n> "

leap_year_check()