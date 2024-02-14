def getPrimeNumbers(n):
    """Add each prime number from 2 to n to a list and return it"""
    #def primeList;
    primeList = []
    # check if number is >1
        #if not, return 0 or some error
    if n < 2:
        return [False]
    for x in range(2,n):
        if primeCheck(x):
            primeList.append(x)
    return primeList

def primeCheck(i):
    """Checks if i is prime and returns true or false"""
#function primeCheck(j) returns true or false
    #if(j == 2)
        #return true
    if i == 2:
        return True
        
    #if(i % 2 == 0)
        #return false
    if i % 2 == 0:
        return False

    #num = j exponent 0.5
    #loop from i = 2; i <= num; i++
        # if(j % i == 0)
            #return false;
    for x in range(2, i):
        if i % x == 0:
            return False
        
    return True
    #return true    

#loop from i = 2 to n; i++
    #if(primeCheck(i))
        #add i to the list
#return list;

print(getPrimeNumbers(1000))
