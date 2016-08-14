# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
# without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers
#  from 1 to 20?

#20 (2*2*5)
#19
#18 (2*3*3)
#17
#16 (2*2*2*2)
#15 (3*5)
#14 (2*7)
#13
#12 (2*2*3)
#11
#  CONTINUE
#9 (3*3)
#8 (2*2*2)
#7
#6 (2*3)
#5
#4 (2*2)
#3
#2

# 1, 2, 3, 5, 7, 11, 13, 17, 19

number = 2*2*2*2*3*3*5*7*11*13*17*19

print number
# Prime Numbers
# 1, 2, 3, 5, 7, 11, 13, 17, 19
# 
# prime_product = 2*3*5*7*11*13*17*19
# 
# print prime_product

# prime_product is not correct

# largest_factors = 11*12*13*14*15*16*17*18*19*20

# print largest_factors

# largest_factors is not correct

# numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# 
# print numbers 
# 
# def multiple():
# 
#     for y in xrange(6000000, 10000000):
#             
#             if y % 20 != 0:
#                 print "1 nope"
#             else:
#                 if y % 19 != 0:
#                     print "2 nope"
#                 else:
#                     if y % 18 != 0:
#                         print "3 nope"
#                     else:
#                         if y % 17 != 0:
#                             print "4 nope"
#                         else:
#                             if y % 16 != 0:
#                                 print "5 nope"
#                             else:
#                                 if y % 15 != 0:
#                                     print "6 nope"
#                                 else:
#                                     if y % 14 != 0:
#                                         print "7 nope"
#                                     else:
#                                         if y % 13 != 0:
#                                             print "8 nope"
#                                         else:
#                                             print y
#                                             return
# 
# multiple()
