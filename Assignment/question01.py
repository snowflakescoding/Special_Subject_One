def ticketValidator(code):
    
    # airline code (first 3 characters) is not allowed: ["VNA", "BAM", "JET", "VJA", "AGR"].
    disallowed_airlines = ["VNA", "BAM", "JET", "VJA", "AGR"]
    
    # airline code must have exactly 8 characters, if not, return False
    if len(code) != 8:
        return False
    
    # first three chars must be uppercase letters
    airline_code = code[0:3]    
    if not (airline_code.isalpha() and airline_code.isupper()): # isalpla: in the alphabetical order, isupper: uppercase
        return False    
    if airline_code in disallowed_airlines: # if in disallowed airlines => False
        return False
    
    # next 4 chars must be one-digit number
    flight_number = code[3:7]
    if not flight_number.isdigit():
        return False
    
    # last character must be an uppercase letter or a digit
    last_character = code[7]
    if not (last_character.isalnum() and last_character.isupper() or last_character.isdigit()): # isalnum(): all characters in a string are alphanumeric
        if last_character.islower():
            return False
        if not last_character.isalnum():
            return False
    
    # airline code must not contain three consecutive identical characters ("AAA1234B" is invalid).
    for i in range(len(code) - 2):
        if code[i] == code [i + 1] and code[i + 1] == code[i + 2]:
            return False
    
    # all conditions met => True
    return True
