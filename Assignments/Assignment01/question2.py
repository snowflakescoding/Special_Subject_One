def ticketValidator2(code):
    
    # create a list of reasons for invalid tickets
    invalid_reason = []

    # add reason "Ticket code must be exactly 8 characters"
    if len(code) != 8:
        invalid_reason.append("Ticket code must be exactly 8 characters")

    # add reason "First 3 characters must be uppercase letters"    
    airline_code = code[0:3]   
    if not (airline_code.isalpha() and airline_code.isupper()): 
        invalid_reason.append("First 3 characters must be uppercase letters")   

    # add reason "Airline code is not allowed"
    if airline_code in ["VNA", "BAM", "JET", "VJA", "AGR"]:
        invalid_reason.append("Airline code is not allowed")

    # add reason "Next 4 characters must be digits"   
    flight_number = code[3:7]
    if not flight_number.isdigit():
        invalid_reason.append("Next 4 characters must be digits")

    # add reason "Last character must be uppercase letter or digit"
    last_character = code[7]
    if not (last_character.isupper() or last_character.isdigit()):
        invalid_reason.append("Last character must be uppercase letter or digit")
        
    # add reason "Ticket code contains three consecutive identical characters"
    for i in range(len(code) - 2):
        if code[i] == code [i+1] == code[i+2]:
            invalid_reason.append("Ticket code contains three consecutive identical characters")
            break 

    # check if the ticket is valid or invalid
    if not invalid_reason:
        return "Valid"
    else:
        return "Invalid. " + ". ".join(invalid_reason)


