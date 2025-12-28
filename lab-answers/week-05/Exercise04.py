"""
Suppose that we have a list of words and a list of letters. We want to find out all words made from letters in the second list and appear in the first list. For example, if the first list is ['fat','tap','day','fun','man','ant','bag','aim'] and the second list is ['m','t','e','d','f','a','p','y','i'] then the result list is: ['fat', 'tap', 'day', 'aim'].

Write a Python function named possibleWords(wordList, charList) that takes two lists - list of words and list of letters as the input and return a list of all words made from letters in the second list and appear in the first list.

We assume that the input list contains at least one integer and all inputs data are correct. 
"""

def possibleWords(wordList, charList):
    # frequency map of available characters
    char_freq = {}
    for char in charList:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    res = []
    
    # check each word in wordList
    for word in wordList:
        # frequency map of available word
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1

        # check if all characters in the word are available with sufficient frequency
        can_make_word = True
        for char, count in word_freq.items():
            if char_freq.get(char, 0) < count:
                can_make_word = False
                break
        
        # word can be made => add to result
        if can_make_word:
            res.append(word)
            
    return res

print(possibleWords(['fat','tap','day','fun','man','ant','bag','aim'],['m','t','e','d','f','a','p','y','i']))