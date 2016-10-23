# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# https://docs.python.org/2/library/calendar.html#module-calendar

import calendar

months = {'jan': 31, 'feb': 28, 'feb_leap': 29, 'mar': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'aug': 31,
'sept': 30, 'oct': 31, 'nov': 30, 'dec': 31}

# normal year is 365 days
# leap year is 366 days

# sunday_start: 19000107

def dayListBuild():

    sunday_count = 0

    start_year = int(raw_input("What year would you like to start with? \n> "))
    start_month = raw_input("Month? \n> ")
    # start_day = int(raw_input(("Day? \n> "))
    end_year = int(raw_input("What year would you like to end with? \n> "))
    end_month = raw_input("Month? \n> ")
    end_day = int(raw_input("Day? \n> "))

    dayListBuild = [[0,0,0]]
    for year in range(start_year, end_year+1):
        for month in range(start_month, end_month+1):
            if month in [4, 6, 9, 11]:
                day_count = 30
            elif month is 2:
                if year % 4 and (not year % 100 or year % 400):
                        dayRange = 29
                else:
                    dayRange = 28
            else:
                dayRange = 31
            for day in range(1, dayRange + 1):
                dayListBuild.append([year, month, day])
    return dayListBuild





def counting_sundays():

    sunday_count = 0

    start_year = int(raw_input("What year would you like to start with? \n> "))
    start_month = raw_input("Month? \n> ")
    # start_day = int(raw_input(("Day? \n> "))
    end_year = int(raw_input("What year would you like to end with? \n> "))
    end_month = raw_input("Month? \n> ")
    end_day = int(raw_input("Day? \n> "))


    while start_year < endyear:
    
        start_year +=1
        
        print start_year
        
        if start_year % 4 != 0:
            continue
                
        elif start_year % 4 == 0 and start_year % 100 == 0 and start_year % 400 != 0:
            continue
            
        else:
            print "Yep,", start_year, "is a leap year. Hooray for an extra day!"

    if day % 7 == 0:
        isSunday = True
        sunday_count += 1
    
counting_sundays()
