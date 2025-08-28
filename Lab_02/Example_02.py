def fizzBuzz():
    # tip: use try-except from the week 2 lecture
    try:
        # print the first line
        number = int(input("Enter a number: "))

        # number < 0 -> print this line
        if number < 0:
            print("The number must be zero or positive")
        
        # after that, do the same thing as refered to the example 01
        else:
            if number % 3 == 0 and number % 5 == 0:
                print("fizzbuzz")
            elif number % 3 == 0:
                print("fizz")
            elif number % 5 == 0:
                print("buzz")
            else:
                print(number)

    except ValueError:
        print("Please enter a number")
