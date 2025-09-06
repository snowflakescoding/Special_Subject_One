# task: read two-digit number

# use readOneDigit function from the part_one.py
def readOneDigit(number):
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    else:
        return 'Invalid digit'

# main part
def readTwoDigits(number):
    # Case 01: number isn't a two-digit one
    if not (0 <= number <= 99): 
        return "Invalid two-digit number"

    # Case 02: number is one-digit one
    if number < 10:
        return readOneDigit(number)

    # Case 03: number is a two-digit from 10 to 19
    elif number >= 10 and number <= 19:
        if number == 10:
            return 'ten'
        elif number == 11:
            return 'eleven'
        elif number == 12:
            return 'twelve'
        elif number == 13:
            return 'thirteen'
        elif number == 14:
            return 'fourteen'
        elif number == 15:
            return 'fifteen'
        elif number == 16:
            return 'sixteen'
        elif number == 17:
            return 'seventeen'
        elif number == 18:
            return 'eighteen'
        else:
            return 'nineteen'
    
    # Case 4: number is a two-digit from 20 to 99
    else:
        tens_digit = number // 10 # find the tens (hàng chục)
        units_digit = number % 10 # find the units (hàng đơn vị)
        
        tens_word = '' # give it a null first
        if tens_digit == 2:
            tens_word = 'twenty'
        elif tens_digit == 3:
            tens_word = 'thirty'
        elif tens_digit == 4:
            tens_word = 'forty'
        elif tens_digit == 5:
            tens_word = 'fifty'
        elif tens_digit == 6:
            tens_word = 'sixty'
        elif tens_digit == 7:
            tens_word = 'seventy'
        elif tens_digit == 8:
            tens_word = 'eighty'
        elif tens_digit == 9:
            tens_word = 'ninety'

        if units_digit == 0: # units_digit = 0 -> twenty, thirty, ...
            return tens_word
        else: # units_digit != 0 -> combine
            return tens_word + ' ' + readOneDigit(units_digit)
