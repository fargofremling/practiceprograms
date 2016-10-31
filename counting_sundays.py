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

# normal year is 365 days
# leap year is 366 days

# sunday_start: 19000107

def dayListBuild():

    sunday_count = 0

    start_year = int(raw_input("What year would you like to start with? \n> "))
    start_month = int(raw_input("Month? \n> "))
    start_day = int(raw_input("Day? \n> "))
    end_year = int(raw_input("What year would you like to end with? \n> "))
    end_month = int(raw_input("Month? \n> "))
    end_day = int(raw_input("Day? \n> "))

    dayListBuild = [[0,0,0]]
    
    a = 0
    
    for year in range(start_year, end_year+1):
        
        for month in range(start_month, end_month+1):
            
            a = a + 6
            
            day_count = 31
            
            if month in [4, 6, 9, 11]:
                day_count = 30
            
            elif month == 2:
                if year % 4 != 0:
                    day_count = 28
                
                elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
                    day_count = 28

                else:
                    print "Yep,", year, "is a leap year. Hooray for an extra day!"
                    day_count = 29
                
            for day in range(start_day, day_count + 1):

                dayListBuild.append([year, month, day])
                # Need to figure out how to write this. 
                if len(dayListBuild) > 6 and dayListBuild[a][2] == 1:
                    print "LOOK RIGHT HERE!!"
                    print dayListBuild[a][2] 
                    print a
                    print day
                    sunday_count += 1
                    print sunday_count
                else:
                    continue   
    print len(dayListBuild)/7
    
    print sunday_count

dayListBuild()

# tried 100, 1200 
# answer should be right around 200