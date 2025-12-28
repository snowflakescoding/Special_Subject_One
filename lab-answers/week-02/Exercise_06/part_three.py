# task: read a four-digit number in English

# from part_one.py
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

# from part_two.py
def readTwoDigits(number):
    if not (0 <= number <= 99):
        return "Invalid two-digit number"

    if number < 10:
        return readOneDigit(number)
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
    else:
        tens_digit = number // 10
        units_digit = number % 10
        
        tens_word = ''
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

        if units_digit == 0:
            return tens_word
        else:
            return tens_word + ' ' + readOneDigit(units_digit)

# main part
def readFourDigits(number):
    if not (0 <= number <= 9999):
        return "Invalid number"

    if number == 0:
        return "zero"

    result = []
    
    thousands = number // 1000
    if thousands > 0:
        result.append(readOneDigit(thousands) + ' thousand')
    
    remainder_hundreds = number % 1000
    hundreds = remainder_hundreds // 100
    
    if hundreds > 0:
        if result:
            result.append('and')
        result.append(readOneDigit(hundreds) + ' hundred')
    
    remainder_tens = remainder_hundreds % 100
    
    if remainder_tens > 0:
        if result and result[-1] != 'and':
            result.append('and')
        
        result.append(readTwoDigits(remainder_tens))
    
    return ' '.join(result)
