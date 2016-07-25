# To determine whether a year is a leap year, follow these steps:
# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).



def leap_year_check():
    
    year = int(raw_input("What year would you like to check. \n> "))
    
    if year % 4 != 0:
        print "Nope, it's not a leap year."
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print "Nope, it's not a leap year."
    else:
        print "Yep, it's a leap year. Hooray for an extra day!"

leap_year_check()
