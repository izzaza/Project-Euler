#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 35 #

# #The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

# In[6]:


def getPrimesBelowN(n=1000000):
    """Get all primes below n with the sieve of Eratosthenes. 
    @return: a list 0..n with boolean values that indicate if 
             i in 0..n is a prime.
    """
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes

def isCircularPrime(primes, number):
    """Check if number is a circular prime.

    Keyword arguments:
    primes -- a list from 0..n with boolean values that indicate if 
              i in 0..n is a prime
    number -- the integer you want to check
    """
    number = str(number)
    for i in range(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True

if __name__ == "__main__":
    print("Start sieving.")
    primes = getPrimesBelowN(1000000)
    print("End sieving.")
    numberOfPrimes = 2
    print(2)    # I print them now, because I want to skip all primes
    print(5)    # that contain one of those digits: 0,2,4,5,6,8
    for prime, isPrime in enumerate(primes):
        if (not isPrime) or ("2" in str(prime)) or            ("4" in str(prime)) or ("6" in str(prime)) or            ("8" in str(prime)) or ("0" in str(prime)) or            ("5" in str(prime)):
            continue
        if isCircularPrime(primes, prime):
            print(prime)
            numberOfPrimes += 1

    print("Number of circular primes: %i" % numberOfPrimes)

