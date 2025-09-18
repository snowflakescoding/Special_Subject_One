# A string is said to be palindrome if the reverse of the string is the same as the string. For example, “abba” is a palindrome because the reverse of “abba” will be equal to “abba”.
# But “abbc” is not a palindrome string.
# task: build a function named isPalindrome. If it's a palindrome, return YES, else, return NO

def isPalindrome(s):
    # declare two pointers
    left = 0 
    right = len(s) - 1
    
    # continue looping while two pointers haven't crossed
    while left < right:
        
        # characters at the current positions aren't equal => not palindrome
        if s[left] != s[right]:
            return 'NO'
        
        # move left to right, move right to left
        left += 1
        right -= 1
        
    # no mismatch is found => palindrome
    return 'YES'
