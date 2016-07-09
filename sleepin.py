day_of_week = raw_input("What day of the week is tomorrow? \n> ").lower()

weekend = [
    "saturday",
    "sat",
    "sunday",
    "sun",
    "s"]

weekday = [
    "monday", "mon", "m",
    "tuesday", "tues", "tue", "t",
    "wednesday", "wed", "w",
    "thursday", "thurs", "thu", 
    "friday", "fri", "f"]


if day_of_week in weekend:
    print "Lucky you! You get to sleep in tomorrow!"
    
elif day_of_week in weekday:
     print "Sucks to be you! Looks like you're getting up early tomorrow!"
     
else:
    print "Hmm, not sure what day you meant. Guess it'll be a surprise."
