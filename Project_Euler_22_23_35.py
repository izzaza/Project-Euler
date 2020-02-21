#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 22 #

# #Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

# In[1]:


#time module for execution time
import time

#time at the start of execution
start = time.time()

#function to return the value of name score
def name_score(name):
    letters = list(name)
    letters = [ord(x)-64 for x in letters]
    return sum(letters)

#reading the contents in the file
with open("C:\\Users\\Lenovo\\Documents\\WORK\\PROJECT KURLOG\\Pelatihan Rosebay\\Task-Project Euler\\p022_names.txt") as f:
    a = f.read()

a = a.strip().split(',')

a = [x[1:-1] for x in a]

#sorting the values of the list
a.sort()

#total score
scores = 0

#counting the total score
for i in range(len(a)):
    scores += name_score(a[i])*(i+1)

#printing the total score
print (scores)

#time at the end of execution
end = time.time()

#total time for execution
print (end-start)


# # PROBLEM 23 #

# #A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number. A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# In[2]:


def GetSumOfDivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return GetSumOfDivs(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}

sums = 1
for i in range(2, 28123):
    boo = True
    for k in lAbundants:
        if k < i:
            if (i-k) in dAbundants:
                boo = False
                break
        else : break
    if boo == True: sums += i

print(sums)


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

