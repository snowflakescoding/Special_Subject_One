"""
In a non-duplicate list, each item value appears only once. For example, [8, 2, 4, 5] is a non-duplicate list, and [3, 0, 2, 3] isn't a non-duplicate list.
task: python function named getNonDuplicateList(n) perform in details:
if the user doesn't enter an integer, the function will print: Please enter an integer
if the integer doesn't exist in the list, the function will include this integer at the end of the list
if the integer exists in the list, the function will print: This number already exists in the list, please enter a new number
if the total number of integers in the list is smaller than n, the function will continue asking the user to enter a new number
if the total number of integers is equal to n, the function will return the list of n integers
"""

def getNonDuplicateList(n):
    # make an empty list 
    non_duplicated_list = []
    
    # continue the loop if length of the list is smaller than n
    while len(non_duplicated_list) < n:
        # use try-except to handle all cases
        try: 
            # declare a number
            number = int(input("Please enter a number: ")) 
            
            # number in the non-duplicated list => already exists
            if number in non_duplicated_list: 
                print("This number already exists in the list. Please enter a new number")
            
            # use append to add a number in
            else: 
                non_duplicated_list.append(number)
        
        except ValueError:
            print("Please enter an integer")
        
    # return the list that we need
    return non_duplicated_list
