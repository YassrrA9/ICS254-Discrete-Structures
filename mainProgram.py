
# Q2. Create an array my_Primes that contains all the primes less than 20.
#  Make a loop that prints these elements one by one. 

my_Primes = [1,2,3,5,7,11,13,17,19]

for x in my_Primes:
    print(x)

print("-----------------------------------------------------------------------------------")


# Q3. Implement the gcd function using the Euclidean Algorithm to compute the gcd(a,b).  


import random
from typing import Counter


first_parameter = int(input("Enter the first number \n"))
second_parameter = int(input("Enter the second number \n"))

def gcd(first_parameter,second_parameter):
    a = first_parameter
    b = second_parameter
    q = a / b
    r = a % b

    if (r == 0):
        return b
    else:
        return gcd(b,r)   
        

print(f"\nThe gcd of {first_parameter} and {second_parameter} is {gcd(first_parameter, second_parameter)}")
print("-----------------------------------------------------------------------------------")


# Q.4 Implement a primality test function is_prime (n, k) based on Fermat Little Theorem, 
# where n is the number to be tested, and k is the number of bases to be used.
#  The function should return False if n is not prime, and True if n is pseudoprime to these k bases. 

def is_prime(n,k):

    if (n == 1) or (n == 4):
        return False
    elif (n <= 3 ):
        return True

    else:
        
        for j in range(k):
            m = random.randint(2, n-2)

            if( (m ** (n-1)) % n) == 1:
                return True
            elif((gcd(n,m)) == 1):
                return True
            else:
                return False


for i in range(2000):
    if( is_prime(i,5)):
        print(f"{i}")



#__________________________________________________________________________________________________________________
#PA2
# Q1. Implement a Boolean function mersenne (p)
#  that returns true if and only if Mp is a Mersenne prime.

def mersenne(p):

    if (is_prime(p,3)):
        M = 2 ** p-1
    else:
        return False
    if (is_prime(M,3)):
        return True


print("-----------------------------------------------------------------------------------")


# Q1.a a)	In the main program, use your function to print all the Mersenne primes
#  Mp for p between 2 and 29, (with k = 3 in the is_prime function). 

print("MERSENNE primes that form 2 - > 29")
def mersennePrimesToBePrinted():
    for number in range(2,30):
        if mersenne(number):
            Mp = (2**number) - 1
            print(f"The number {Mp} is the MERSENNE prime of length {number}")


mersennePrimesToBePrinted()
# Q1.d d) Test mersenne (31). 

print("-----------------------------------------------------------------------------------")

def toTest():
    timeToBEComputed = timeit.timeit(stmt='mersenne(31)', globals=globals(), number=1)
    print(f" The time taken to compute MERSENNE(31) is {timeToBEComputed} seconds")


toTest()

print("-----------------------------------------------------------------------------------")


# Q2. Implement the modular exponentiation (a.k.a. fast exponentiation) function mod_exp (b, n, m) 
# to compute bn (mod m) more efficiently. 

def mod_exp(b,n,m):

    i = 1

    if 1 & n:
        i = b
    
    while n:
        n >>= 1
        b = (b * b)%m
        if n & 1:
            x = ( x*b)%m
    return x

print("-----------------------------------------------------------------------------------")

# a)	Test your function for b = 3,  n = 231 – 2, m = 231 – 1. 

def mod_exp_ToBeTested():
    m = ( 2**31) - 1
    b = 3
    n = ( 2**31) - 2
    result = mod_exp(b,n,m)
    startPoint = time.time()
    timeOccur = time.time() - startPoint
    print(f"Time spent on computed mod_exp is {timeOccur}")


mod_exp_ToBeTested()

print("-----------------------------------------------------------------------------------")



# Q3. Modify your is_prime function to use the mod_exp (b, n, m) 
# instead of the standard power operation (b**n % m). 
# Rename it as is_prime2. Modify the mersenne (p) function to use is_prime2, 
# and call it mersenne2. 

def is_prime2(n,k):

    if ( n == 1):
        return False
    elif (( n < 20 ) and ( n in my_Primes)):
        return True
    
    for x in range(k):
        l = random.randint(2,n-2)
        if ( n % 2 != 1):
            return False
        elif ( mod_exp( l,n-1,n) != 1):
            return False
    
    return True


def is_prime2_ToBeTested():
    print("print all primes up to 2000 using is_prime2")
    k = 7
    counter = 0
    for i in range(1, 2000):
        if is_prime2(i, k):
            print(i, " is prime")
            counter += 1
    print(counter)

print("-----------------------------------------------------------------------------------")

def mersenne2(p):
    if is_prime2(p, 3):
        M = (2**p) - 1
    else:
        return False
    if is_prime2(M, 3):
        return True


def mersenne_primes2_ToBeTested():

    for number in range(2, 100000):
        if mersenne2(number):
            Mp = (2**number) - 1
            print(f" {Mp} is the MERSENNE prime pf the length {number}")


mersenne_primes2_ToBeTested()

print("-----------------------------------------------------------------------------------")

print(f"\nThe gcd of {first_parameter} and {second_parameter} is {gcd(first_parameter, second_parameter)}")




