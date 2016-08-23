# Problem #10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


n = int(raw_input("What prime number would you like to find?\n> "))

primes = []

for p in range(2, n+1):

    for x in range(2, p):
    
         if p % x == 0:
             break
    else:
        print p
        primes.append(p)
            
print primes
         
def add(x, y):
    return x + y

sum = reduce(add, primes)

print sum


#   2   3   5   7   11   13   17   19   23   29   31   37   41   43   47   53   59   61   67   71   73   79   83   89   97   101   103   107   109   113   127   131   137   139   149   151   157   163   167   173   179   181   191   193   197   199   211   223   227   229   233   239   241   251   257   263   269   271   277   281   283   293   307   311   313   317   331   337   347   349   353   359   367   373   379   383   389   397   401   409   419   421   431   433   439   443   449   457   461   463   467   479   487   491   499   503   509   521   523   541  