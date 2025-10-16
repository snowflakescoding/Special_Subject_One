"""
Given a sentence and an integer k, we want to find out the top k most frequent words in the sentence.
Write a Python function named topKWords(sentence, k) that takes a string sentence and an integer k as the input and return a list of tuples that contains the top k most frequent words.
Each item of returned list is a tuple contains a word and the frequency of the word in the input string. The words are sorted by the frequency from highest to lowest. Words with the same frequency is sorted by their lexicographical order.
For example:
if sentence = 'the day is sunny the the the sunny is is' and k = 3 then function returns the following list: [('the', 4), ('is', 3), ('sunny', 2)]
if sentence = 'i love python i love coding' and k = 2 then function returns the following list: [('i': 2), ('love' : 2)]. Note that 'i' comes before 'love' due to a higher alphabetical order.

We assume that the input list contains at least one integer and all inputs data are correct.
"""

def topKWords(sentence, k):
    # split sentence into words
    words = sentence.split()
    
    # word frequencies in dictionary
    word_freq = {}
    
    # count frequency of each word
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # a list of tuples (word, frequency)
    sorted_words = sorted(
        word_freq.items(),
        key =lambda x: (-x[1], x[0])
    )
    
    # return top k words
    return sorted_words[:k]

