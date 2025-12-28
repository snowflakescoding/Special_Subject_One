# Write a Python3 function named dotProduct(a, b) that takes two lists a and b as the inputs, where a and b are two lists of integers and have the same size. 
# The function will calculate and return the value of the dot product between a and b.

def dotProduct(a, b):
    dotProductValue = 0 # initiate value 0 for the product
    for i in range(len(a)): # use for-loop in this exercise
        dotProductValue += a[i] * b[i] # formula to calculate dot product
    return dotProductValue # return the value 
