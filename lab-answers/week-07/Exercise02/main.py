"""
Write a Python3 function named longestWord(fname) that takes a file name of a text file, a String fname, as an argument and find the longest word in the file. A word is a set of consecutive characters without any spaces.
The function will return the longest word found in the input text file. If multiple words share the same longest length, the first one encountered will be returned.
We assume that user always call the function with a correct argument. Please refer to the example table about the input and output of the function.

In this example, the content of the text file test01.txt is:

Example Line 1
Example Line 2
Example Line 3

The function will return Example when calling: longestWord('test01.txt') 
"""

def longestWord(fname):
    longest = ""
    
    with open(fname, 'r') as file:
        for line in file:
            words = line.split()
            
            for word in words:
                if len(word) > len(longest):
                    longest = word
    
    return longest

print(longestWord('test01.txt'))
print(longestWord('test02.txt'))
print(longestWord('test03.txt'))
print(longestWord('test04.txt'))