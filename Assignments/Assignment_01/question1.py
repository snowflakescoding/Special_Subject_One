def ticketValidator(code):
        
    # airline code must have exactly 8 characters
    if len(code) != 8:
        return False
    
    airline_code = code[0:3] 
    # airline code must be uppercase letters
    if not (airline_code.isalpha() and airline_code.isupper()): 
        return False    
    
    # airline codes are not allowed: ["VNA", "BAM", "JET", "VJA", "AGR"]
    if airline_code in ["VNA", "BAM", "JET", "VJA", "AGR"]: 
        return False
    
    flight_number = code[3:7]
    # next 4 chars must be one-digit number
    if not flight_number.isdigit():
        return False
    
    last_character = code[7]
    # last character must be an uppercase letter or a digit
    if not (last_character.isupper() or last_character.isdigit()):
        return False
    
    # airline code must not contain three consecutive identical characters
    for i in range(len(code) - 2):
        if code[i] == code [i+1] == code[i+2]:
            return False
    
    # all conditions met => True
    return True
