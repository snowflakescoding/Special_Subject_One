# task: build a python function that takes 3 values from Pythagorean Triplets

def pythagoreanTriplets(num):
    # tip: use nested for-loop
    """
    note: 
    a must be between 1 and num
    b must be between a and num
    c must be between b (excluded) and num
    """
    for a in range(1, num + 1):
        for b in range(a, num + 1):
            for c in range(b + 1, num + 1):
                if a * a + b * b == c * c: # check if it is a Pythagorean Triplets 
                    print(f"({a}, {b}, {c})") # use printf
