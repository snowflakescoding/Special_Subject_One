"""
Write a Python3 function named combineFile that accepts the names of two text files as arguments and performs the following actions:

The function will read the content of both files line by line, then combine each pair of lines.
All combined lines will be merged into a single string, with each combined line separated by a space character.
The function will then return the merged string.
We assume that the two text files have the same number of lines, and the user always call the function with a correct argument. 

For example, if the content of test05.txt is:
ABC
DEF
GHK

and the content of test06.txt is:
abc
def
ghk

then when you call combineFile('test05.txt','test06.txt'), the function will return the following string:
'ABC abc DEF def GHK ghk'
"""

def combineFile(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    combined_lines = []
    for line1, line2 in zip(lines1, lines2):
        combined = line1.strip() + ' ' + line2.strip()
        combined_lines.append(combined)
    
    res = ' '.join(combined_lines)
    
    return res

print(combineFile('test05.txt', 'test06.txt'))
print(combineFile('test07.txt', 'test08.txt'))
print(combineFile('test05.txt', 'test07.txt'))
print(combineFile('test06.txt', 'test08.txt'))
