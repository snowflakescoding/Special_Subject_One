"""
In this step, we will create a function named convertWordToPigLatin(word) to convert the input word into Pig Latin form. We consider the following cases: 

- If the word doesn't have a vowel, then convertedWord = 'yayyay'
- If the word starts with a vowel, then convertedWord = word + 'yay'
- If the word begins with a consonant or more than one consonant, then we will form convertedWord based on the conversion rule

In any case, the function will return the convertedWord. You should use the helper function findFirstVowel() from step 1 when creating the function convertWordToPigLatin().
"""

# use from hint_one.py
def findFirstVowel(word):
    vowels = "aeiouAEIOU"
    for i in range (len(word)):
        if word[i] in vowels:
            return i
    return -1
    
# hint_two.py
def convertWordToPigLatin(word):
    # call out the index of the first vowel of the word
    index_first_vowel = findFirstVowel(word)
    
    # no vowel in that word, return 'yayyay'
    if index_first_vowel == -1: 
        return 'yayyay'

    # word starts with a vowel, return word + 'yay'
    elif index_first_vowel == 0:
        return word + 'yay'
    
    # word starts with a consonant / > 1 consonant, use conversion rule
    else:
        consonant = word[:index_first_vowel]
        remained_word = word[index_first_vowel:]
        return remained_word + consonant + 'ay'
        
