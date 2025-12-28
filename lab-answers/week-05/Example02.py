"""
In a string, the most frequent character is the character that the highest frequency in a string, except the space character.
Write a Python3 function named mostFrequentChar(sentence) that take a sentence as the input and returns the most frequent character in the sentence. If there are many characters that have the same highest frequency, the function will return the left most character.
For example:
mostFrequentChar('i love python') will return character 'o'
mostFrequentChar('apple is good') will return character 'p'

We assume that the input sentence contains only lowercase characters and all inputs data are correct
"""

def mostFrequentChar(sentence):
    # store character frequencies
    char_freq = {}
    
    # count frequency of each character
    for char in sentence:
        if char != ' ':
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # find max frequency
    max_freq = max(char_freq.values())
    
    # find leftmost character with max frequency
    for char in sentence:
        if char != ' ' and char_freq[char] == max_freq:
            return char
        
