"""
Suppose X is a list of positive integers, each of which is smaller than 1000.
We define max to be the largest possible number using the elements of X. For example, 
If X = [8, 4, 2, 9, 5, 6, 1, 0], then max = 98654210
If X = [1, 4, 20, 399, 50, 6], then max = 6504399201
If X = [320, 400, 41, 4, 745, 9], then max = 9745441400320

Create a Python3 function named maxPermutation(list) that takes a list as its argument # and returns the max value.
"""

def maxPermutation(list):
    # convert number to a string
    str_nums = [str(num) for num in list]
    n = len(str_nums)
    
    # track if any swaps were made
    swapped = True
    
    # use bubble sort
    while swapped: 
        swapped = False
        for i in range(n - 1):
            # compare adjacent elements, then swap
            if str_nums[i] + str_nums[i+1] < str_nums[i+1] + str_nums[i]:
                str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                swapped = True

    # join and return the result
    return int("".join(str_nums))

                
