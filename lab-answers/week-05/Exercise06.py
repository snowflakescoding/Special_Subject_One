"""
Suppose that we use a nested dictionary to store the data about students, for example:

students = { 'std001': {'info': {'name': 'John', 'age': 27, 'sex': 'Male'}, 'gpa' : 3.2},
             'std002': {'info': {'name': 'Marie', 'age': 22, 'sex': 'Female'}, 'gpa' : 3.5},
             'std003': {'info': {'name': 'Peter', 'age': 23, 'sex': 'Male'}, 'gpa' : 3.1} }

An item in students dictionary is a pair {key, value} where key is student ID such as 'std001', 'std002', ... and value is a dictionary contains information about the student. This dictionary is also a nested dictionary.

Write a Python function named searchForStudent(students, key, value) that takes a student nested dictionary and pair (key, value) as a search condition and return a list of student IDs that satisfies the condition. The function will return -1 if it couldn't find any student.

We assume that the input list and all inputs data are correct.
"""

def searchForStudent(students, key, value):
    res = []
    
    # iterate through each student
    for student_id, student_data in students.items():
        # check if the key is gpa
        if key == 'gpa':
            if student_data.get('gpa') == value:
                res.append(student_id)
        
        # if not, search in the 'info' nested dictionary
        else:
            if 'info' in student_data:
                if student_data['info'].get(key) == value:
                    res.append(student_id)
    
    # return the result list or -1 if no matches found
    return res if res else -1