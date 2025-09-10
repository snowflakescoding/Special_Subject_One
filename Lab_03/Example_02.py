#task: python function that asks user to input an integer which must be an odd number from 1 to 50.

def inputValidation():
    while True:
        try:
            number = int(input("Enter a odd integer from 1 to 50: ")) # input a number
            
            if number < 1 or number > 50: # case 1: out of the range between 1 and 50
                print("The number must be an odd number from 1 to 50")
            
            elif number % 2 == 0: # case 2: if case 1 passes, case 2 will check if it is an odd or even number. if even = print the same line as the first case
                print("The number must be an odd number from 1 to 50")
            
            else: # case 3: if case 1 and 2 are all passed
                return number
                
        except ValueError:
            print("Please enter an integer")

# process: while loop -> try/except -> follow the question
