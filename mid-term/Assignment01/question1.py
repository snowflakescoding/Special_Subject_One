def ticketValidator(code):
        
    # airline ticket must have exactly 8 characters
    if len(code) != 8:
        return False
    
    # check if airline code are uppercase letters
    airline_code = code[0:3] 
    if not (airline_code.isalpha() and airline_code.isupper()): 
        return False    
    
    # check if in disallowed airline code: ["VNA", "BAM", "JET", "VJA", "AGR"]
    if airline_code in ["VNA", "BAM", "JET", "VJA", "AGR"]: 
        return False
    
    # check if flight numbers are one-digit 
    flight_number = code[3:7]
    if not flight_number.isdigit():
        return False
    
    # check if last character is an uppercase letter or a digit
    last_character = code[7]
    if not (last_character.isupper() or last_character.isdigit()):
        return False
    
    # check if airline code contain three consecutive identical characters
    for i in range(len(code) - 2):
        if code[i] == code [i+1] == code[i+2]:
            return False
    
    # all conditions met => True
    return True

