"""
Suppose that we are required to model students and teachers in our application.

We can define a superclass called Person to store common properties like name and address, and subclasses Student and Teacher for their specific properties.
For students, we need to maintain the courses taken and their respective grades, add a course with a grade, and print all courses taken with the average grade. Assume that a student takes no more than 30 courses for the entire program.
For teachers, we need to maintain the current teaching course and be able to add or remove a taught course. Assume that a teacher teaches not more than 5 courses concurrently.

Write the code for the Person, Student, and Teacher classes.
"""

# Person class
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def getName(self):
        return self.name
        
    def getAddress(self):
        return self.address
        
    def setAddress(self, address):
        self.address = address
    
    def __str__(self):
        return f"{self.name}({self.address})"

# student class inherited from person class
class Student(Person):
    max_course = 30 # max courses a student can take
    
    def __init__(self, name, address):
        super().__init__(name, address) 
        self.numCourses = 0
        self.courses = [] 
        self.grades = [] 
        
    def __str__(self):
        return f"Student: {super().__str__()}"
        
    def addCourseGrade(self, course, grade):
        if self.numCourses < Student.max_course:
            self.courses.append(course)
            self.grades.append(grade)
            self.numCourses += 1
            
    def printGrades(self):
        grades_output = []
        for course, grade in zip(self.courses, self.grades):
            grades_output.append(f"{course} : {grade}")
        print(" | ".join(grades_output) + " |")
        
    def getAverageGrade(self):
        if self.numCourses == 0:
            return 0.0
        return sum(self.grades) / self.numCourses
            
# teacher class inherited from person
class Teacher(Person):
    concurrently_course = 5 # teach not more than 5 courses concurrently
    
    def __init__(self, name, address):
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = [] 
        
    def __str__(self):
        return f"Teacher: {super().__str__()}"
        
    def addCourse(self, course):
        if course in self.courses:
            return False 
        if self.numCourses >= Teacher.concurrently_course:
            return False 
            
        self.courses.append(course)
        self.numCourses += 1
        return True
        
    def removeCourse(self, course):
        try:
            self.courses.remove(course)
            self.numCourses -= 1
            return True
        except ValueError:
            return False
