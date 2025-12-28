"""
When processing text data with Python, a word is defined as a sequence of non-space characters. A sentence is defined as a sequence of words that is separated by at least one space.
Write a Python3 function named wordCount(sentence) that takes a sentence as input and returns two integers:
- The total number of words in this sentence
- The total number of characters (without spaces) in this sentence
For example, wordCount('I love Python') will return (3, 11)
"""
def wordCount(sentence):
  # split the sentence to get individual words
  words = sentence.split()
  # count number of words
  num_words = len(words)
  # count total characters
  num_chars = len(sentence.replace(' ', ''))

  return (num_words, num_chars)
  
