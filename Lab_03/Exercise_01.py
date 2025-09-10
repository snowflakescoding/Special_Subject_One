# task: build a python function to check whether a number is a prime number or not

import math # this is used for finding square root of a number

def isPrime(num):
    if num < 1: # case 1: num is not a positive integer
        return False
    else: # case 2: if case 1 passed successfully
        for i in range(2, int(math.sqrt(num)) + 1): # use for-loop, start: 2 and end: square root of num + 1
            if num % i == 0: # if there are divisors
                return False
        return True # if there are not any divisors
