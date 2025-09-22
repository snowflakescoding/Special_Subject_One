"""
Suppose that C1 and C2 are two non-duplicated lists that contain string items. We define the following operators between the two list:

C1 x C2 returns a list that includes all items that appear in both C1 and C2 (1)
C1 / C2 returns a list that includes all items that appear in C1 but don’t appear in C2 (2)
C1 u C2 returns a list that includes all items that appear in C1 or in C2, except the items that appear in both C1 and C2 (3)

Write a Python3 function named setOperator(list1, list2, operator) that has three parameters:
1. list1 and list2 are two lists of string items
2. operator is a string that has the value 'x', '/', or 'u'. This parameter indicates which operator from the three operators above we want to perform on the two strings.
"""

def setOperator(list1, list2, operator):
    # convert list to set
    set1 = set(list1)
    set2 = set(list2)
    set_result = set()
    
    # use if-elif-else for checking with operators
    if operator == 'x':
        set_result = set1.intersection(set2) # (1)
    elif operator == '/':
        set_result = set1.difference(set2) # (2)
    elif operator == 'u':
        set_result = set1.symmetric_difference(set2) # (3)
    else: 
        print(f"Warning: Unknown operator '{operator}'")
    
    return sorted(list(set_result))
