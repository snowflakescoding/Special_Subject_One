# task: build a sentinel input function in python

def sentinelInput():
    # step 1: start the sum and count with 0
    total_sum = 0
    count = 0
    
    # step 2: while the function happens, use try-except
    while True:
        try: 
            number = int(input("Enter a positive integer: ")) # input a number
            
            # case 1: number is negative
            if number < 0: 
                print("The number must be positive")
            
            # case 2: number is 0 -> count is also 0, avg = 0 and count isn't 0, return the avg and round by 2 decimal numbers
            elif number == 0: 
                if count == 0:
                    return 0
                return round((total_sum / count), 2)
            
            # case 3: if the number is positive
            else: 
                total_sum += number
                count += 1
        except ValueError: # if the input is not a number
            print("Please enter a number") 
