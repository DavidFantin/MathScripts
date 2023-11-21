# Python Program to check whether 
# number is semiprime or not 
import math
# Checks if the number (n) inputed is even
# False -> n is NOT prime
# True  -> n COULD be prime
def EvenCheck (n):
    nCheck = n % 2
    if (nCheck == 1) and (n != 2):
        return False
    else:
        return True

def PrimeCheck(n):
    for x in range(2, math.ceil(math.sqrt(n))):
        nCheck = n % x
        if (nCheck != 0):
            return False
        else:
            pass
    return True

# Driver code 
if __name__ == "__main__":
    n = int(input("Enter a number to check: "))
    #semiprime(n) 
    #prime(n)
    PC = PrimeCheck(n)
    if(PC == True):
        print(n,"is prime")
    else:
        print(n,"is not prime")
    input("Press Enter to Continue...")

















