"""
Write a Python3 function named fileLength(fname) that takes a file name of a text file, a String fname, as an argument and count the total number of lines in this text file:
The function will return the total number of lines in the input text file.
We assume that user always call the function with a correct argument. Please refer to the example table about the input and output of the function.

In this example, the content of the text file test01.txt is:

Example Line 1
Example Line 2
Example Line 3

The function will return 3 when calling: fileLength('test01.txt') 
"""

def fileLength(fname):
    with open(fname, 'r') as file:
        lines = file.readlines()  
        return len(lines)
    
print(fileLength('test01.txt'))
print(fileLength('test02.txt'))
print(fileLength('test03.txt'))
print(fileLength('test04.txt'))

    