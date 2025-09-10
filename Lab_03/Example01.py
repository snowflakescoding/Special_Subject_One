# task: python function for sum of squares using for-loop

def sumOfSquares(n):
    sum = 0 # initiate value 0 to sum
    for i in range(1, n + 1): # run from 1 to n + 1 (excluded):
        sum += i * i # code to calculate sum of squares
    return sum # do not drop in inside the loop

# note: sum of squares from 1 to n is sum = (n * (n + 1) * (2 * n + 1)) / 6
