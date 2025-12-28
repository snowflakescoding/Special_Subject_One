"""
Write a Python 3 function named searchForWord that accepts a word and the name of a text file as arguments. This function should count the number of occurrences of the specified word in the text file and return the count. 
For simplicity, assume the search is not case-sensitive, and the function will always be called with correct arguments. 

For example, the content of test01.txt is:
Example Line 1
Example Line 2
Example Line 3

When calling searchForWord('line','test01.txt'), the function will return the following:
3
"""

import re

def searchForWord(word, filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    content_lower = content.lower()
    word_lower = word.lower()
    
    words = re.findall(r'\b\w+\b', content_lower)
    count = words.count(word_lower)
    
    return count

print(searchForWord('line','test01.txt'))
print(searchForWord('PYTHON','test02.txt'))
print(searchForWord('python','test03.txt'))
print(searchForWord('Python','test04.txt'))
