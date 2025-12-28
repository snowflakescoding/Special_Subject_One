"""
In step 1, we will create a function named findFirstVowel(word) to find the index of the first vowel in the input word. 
If the word starts with a vowel, the function will return 0. 
If the word doesn't have a vowel, the function will return -1. 
"""

def findFirstVowel(word):
    # define all vowels in the alphabet, both upper and lower-case
    vowels = "aeiouAEIOU" 
    
    # use for loop, range is the length of the word
    for i in range (len(word)):
        # index of that word is a vowel, return that index
        if word[i] in vowels:
            return i
    return -1 # word does not have a vowel
    
