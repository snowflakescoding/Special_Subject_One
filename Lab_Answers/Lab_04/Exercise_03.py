# Write a Python3 function named caesarEncoder(word, offset) that has two parameters: word is a word in uppercase, and offset is the shift distance in encryption with the Caesar code. 
# The function will encrypt the input word and return the encrypted word.

def caesarEncoder(word, offset):
    # declare encoded text to nothing
    encodedText = "" 
    
    # use for loop
    for char in word: 
        # case: character is from "a" to "z" (lowercase)
        if "a" <= char <= "z":
            shiftChar = ord("a") + (ord(char) - ord("a") + offset) % 26
            encodedText += chr(shiftChar)
        
        # case: character is from "A" to "Z" (uppercase)
        elif "A" <= char <= "Z":
            shiftChar = ord("A") + (ord(char) - ord("A") + offset) % 26
            encodedText += chr(shiftChar)

        # case: none of the cases are passed
        else: 
            encodedText += char
    
    # return the encoded text
    return encodedText
