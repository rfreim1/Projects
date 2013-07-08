#the user enter a number and find all Prime Factors (if there are any) 
#and display them.
from math import floor, sqrt
print "Enter a number and all prime factor will be found."
number = input("Enter number: ")

def prime_factorize(num):
        factors = []
        half_way = int(floor( sqrt(num) ) )
        for n in range(2, half_way+1):
                if num % n == 0:
                        x = num/n
                        factors.extend(prime_helper(x))
                        factors.extend(prime_helper(n))
        return factors


def prime_helper(x):
        xp = prime_factorize(x)
        if len(xp) == 0:
                return [x]
        else:
                return xp

def prime_wrapper(num):
        x = prime_factorize(number)
        x = set(x)
        if len(x) == 0:
                print "No prime factors of " + str(number) + ". (It is prime)"
        else:
                print "Prime Factors: " + str(list(x))

prime_wrapper(number)
