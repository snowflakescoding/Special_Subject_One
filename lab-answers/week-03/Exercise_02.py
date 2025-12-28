# task: build a python function for half pyramid of numbers

def halfPyramid(rows):
    # tip: use nested for-loop
    for i in range(1, rows + 1): # outer loop, print the number of rows
        for j in range(1, i + 1): # inner loop, print the numbe of column (column here refers to i)
            print(j, end=" ") # print the column, with 1 space added in
        print() # final print, MUST print after declaring the inner loop
        
