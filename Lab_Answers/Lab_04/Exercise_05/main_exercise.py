"""
In this step, we will create the final function convertSentenceToPigLatin(sentence) to convert the whole input sentence into Pig Latin form. In the function, we will deal with the following tasks:

- Break the sentence into a list of words. The built-in string function split() may come in handy
- For each word in words, we convert the word into Pig Latin form using the function convertWordToPigLatin() from step 2. Then extend the converted sentence with the converted word

The function will return the converted sentence as the output.
"""

# use from hint_one.py
def findFirstVowel(word):
    vowels = "aeiouAEIOU"
    for i in range (len(word)):
        if word[i] in vowels:
            return i
    return -1
    
# use from hint_two.py
def convertWordToPigLatin(word):
    index_first_vowel = findFirstVowel(word)
    
    if index_first_vowel == -1: 
        return 'yayyay'
    elif index_first_vowel == 0:
        return word + 'yay'
    else:
        consonant = word[:index_first_vowel]
        remained_word = word[index_first_vowel:]
        return remained_word + consonant + 'ay'

# final part of the pig latin code
def convertSentenceToPigLatin(sentence):
    words = sentence.split()
    converted_words = [convertWordToPigLatin(word) for word in words]
    return ' '.join(converted_words)
