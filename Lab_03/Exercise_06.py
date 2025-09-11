"""
task: generate random numbers that work in this process:

1. continuously generate random numbers in range [left, right]
2. stop generating number when there are exactly 5 integers that are divisible by 5 in the list of generated numbers.
3. combine all generated numbers into a string with a space between numbers and return the string
"""

# tip: use while loop 

import random # the import to get random numbers
def genRandomIntegers(left, right):
    generated_num = [] # array for the generated numbers
    divisible_by_five_count = 0 # initiate the count of numbers % 5 == 0
    
    while divisible_by_five_count < 5: # 
        random_number = random.randint(left, right) # create a random number using random.randint
        generated_num.append(random_number) # add a random number into the array
        
        if random_number % 5 == 0:
            divisible_by_five_count += 1 # random number divisible by 5 -> +1 count 
    
    result_string = ' '.join(map(str, generated_num)) # a way to convert a list of numbers to a space-seperated string
    return result_string
        
