"""
Suppose that C1 and C2 are two non-duplicated lists that contain string items. We define the following operators between the two list:

C1 x C2 returns a list that includes all items that appear in both C1 and C2 (1)
C1 / C2 returns a list that includes all items that appear in C1 but don’t appear in C2 (2)
C1 u C2 returns a list that includes all items that appear in C1 or in C2, except the items that appear in both C1 and C2 (3)

Write a Python3 function named setOperator(list1, list2, operator) that has three parameters:
1. list1 and list2 are two lists of string items
2. operator is a string that has the value 'x', '/', or 'u'. This parameter indicates which operator from the three operators above we want to perform on the two strings.
"""

def setOperation(list1, list2, operator):
    if operator == 'x':
        return [item for item in list1 if item in list2] # intersect way
    elif operator == '/':
        return [item for item in list1 if item not in list2] # difference way
    elif operator == 'u':
        return [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1] # symmetric difference way
    else: 
        return []
