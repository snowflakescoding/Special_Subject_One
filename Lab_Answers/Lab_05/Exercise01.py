"""
Given list of integers, we want to group items that have the same values into groups.
Write a Python function named itemGrouping(inputList) that takes a list of integers as the input and return a dictionary that contains the grouped integers. For each item of the dictionary, the key is an integer in the input list and the value is a list that contains all the integers grouped together on occurrences.
For example:
if inputList = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] then the function will return {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
if inputList = [7, 7, 7, 7] then the function will return {7: [7, 7, 7, 7]}

We assume that the input list contains at least one integer and all inputs data are correct. 
"""

def itemGrouping(inputList):
    
    # dictionary of grouped items
    group_item = {}
    
    for item in inputList:    
        # item not in the grouped item => empty array
        if item not in group_item:
            group_item[item] = []
        # item in the grouped item => add item
        group_item[item].append(item)
    
    # return value
    return group_item

