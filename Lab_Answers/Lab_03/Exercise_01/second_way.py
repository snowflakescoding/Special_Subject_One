# task: build a python function to check whether a number is a prime number or not

# 2nd way: not importing math

def isPrime(n): 
    if n < 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: 
                return False
        return True
