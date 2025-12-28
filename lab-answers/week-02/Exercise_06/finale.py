def readFourDigits(number: int) -> str:
    if number == 0:
        return "zero"

    result = ""
    
    # Process the thousands place
    thousands = number // 1000
    if thousands > 0:
        if thousands == 1:
            result += 'one thousand'
        elif thousands == 2:
            result += 'two thousand'
        elif thousands == 3:
            result += 'three thousand'
        elif thousands == 4:
            result += 'four thousand'
        elif thousands == 5:
            result += 'five thousand'
        elif thousands == 6:
            result += 'six thousand'
        elif thousands == 7:
            result += 'seven thousand'
        elif thousands == 8:
            result += 'eight thousand'
        elif thousands == 9:
            result += 'nine thousand'

    remainder = number % 1000

    # Process the hundreds place
    hundreds = remainder // 100
    if hundreds > 0:
        if len(result) > 0:
            result += ' and '
        
        if hundreds == 1:
            result += 'one hundred'
        elif hundreds == 2:
            result += 'two hundred'
        elif hundreds == 3:
            result += 'three hundred'
        elif hundreds == 4:
            result += 'four hundred'
        elif hundreds == 5:
            result += 'five hundred'
        elif hundreds == 6:
            result += 'six hundred'
        elif hundreds == 7:
            result += 'seven hundred'
        elif hundreds == 8:
            result += 'eight hundred'
        elif hundreds == 9:
            result += 'nine hundred'

    remainder %= 100

    # Process the tens and ones places
    if remainder > 0:
        if len(result) > 0:
            result += ' and '
        
        if remainder < 20:
            if remainder == 1:
                result += 'one'
            elif remainder == 2:
                result += 'two'
            elif remainder == 3:
                result += 'three'
            elif remainder == 4:
                result += 'four'
            elif remainder == 5:
                result += 'five'
            elif remainder == 6:
                result += 'six'
            elif remainder == 7:
                result += 'seven'
            elif remainder == 8:
                result += 'eight'
            elif remainder == 9:
                result += 'nine'
            elif remainder == 10:
                result += 'ten'
            elif remainder == 11:
                result += 'eleven'
            elif remainder == 12:
                result += 'twelve'
            elif remainder == 13:
                result += 'thirteen'
            elif remainder == 14:
                result += 'fourteen'
            elif remainder == 15:
                result += 'fifteen'
            elif remainder == 16:
                result += 'sixteen'
            elif remainder == 17:
                result += 'seventeen'
            elif remainder == 18:
                result += 'eighteen'
            elif remainder == 19:
                result += 'nineteen'
        else:
            tens = (remainder // 10) * 10
            ones = remainder % 10
            
            if tens == 20:
                result += 'twenty'
            elif tens == 30:
                result += 'thirty'
            elif tens == 40:
                result += 'forty'
            elif tens == 50:
                result += 'fifty'
            elif tens == 60:
                result += 'sixty'
            elif tens == 70:
                result += 'seventy'
            elif tens == 80:
                result += 'eighty'
            elif tens == 90:
                result += 'ninety'
            
            if ones > 0:
                result += ' '
                if ones == 1:
                    result += 'one'
                elif ones == 2:
                    result += 'two'
                elif ones == 3:
                    result += 'three'
                elif ones == 4:
                    result += 'four'
                elif ones == 5:
                    result += 'five'
                elif ones == 6:
                    result += 'six'
                elif ones == 7:
                    result += 'seven'
                elif ones == 8:
                    result += 'eight'
                elif ones == 9:
                    result += 'nine'

    return result.strip()


