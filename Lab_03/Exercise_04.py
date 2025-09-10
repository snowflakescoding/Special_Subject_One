# task: count prime numbers in python

def isPrime(n): # use from Exercise 01
    if n < 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: 
                return False
        return True
            
def countPrime(left, right): # main part
    prime_count = 0
    for number in range(left, right + 1): 
        if isPrime(number):
            prime_count += 1 
    return prime_count
