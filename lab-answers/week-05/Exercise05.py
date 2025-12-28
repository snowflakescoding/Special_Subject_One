"""
Find items in a nested dictionary
Suppose that we use a nested dictionary to store the data about students, for example:

students = { 'std001': {'info': {'name': 'John', 'age': 27, 'sex': 'Male'}, 'gpa' : 3.2},
             'std002': {'info': {'name': 'Marie', 'age': 22, 'sex': 'Female'}, 'gpa' : 3.5},
             'std003': {'info': {'name': 'Peter', 'age': 23, 'sex': 'Male'}, 'gpa' : 3.1} }

An item in students dictionary is a pair {key, value} where key is student ID such as 'std001', 'std002', ... and value is a dictionary contains information about the student. This dictionary is also a nested dictionary.

Write a Python function named findStudentByID(students, stdID) that takes a student nested dictionary and a student ID as the input then returns a dictionary that contains data of the corresponding student. The function will return -1 if it couldn't find a student with the input ID.

We assume that the input list and all inputs data are correct. 
"""

def findStudentByID(students, stdID):
    student_data = students.get(stdID, -1)
    return student_data

