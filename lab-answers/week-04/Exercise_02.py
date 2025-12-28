# Write a Python3 function named sortList(listString) that has a parameter listString. It is a list of many items, each of which is a string.
# The function sorts all items in listString in ascending order of the length of each item. The function then returns the sorted list.

def sortList(listString):
    listString.sort(key=len) # use sort method, then sort by length of elements (use key=len)
    return listString # return the sorted list
