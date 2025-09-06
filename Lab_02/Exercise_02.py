#task: build a GPA converter on a 10-point scale.
def gpaConverter(gpa):
    try:
        if gpa < 0 or gpa > 10: 
            return 'Please enter a gpa score in 10-point scale'
        else: 
            if gpa >= 9.0 and gpa <= 10:
                return 4.0
            elif gpa >= 8.5 and gpa < 9.0:
                return 3.7
            elif gpa >= 8.0 and gpa < 8.5:
                return 3.5
            elif gpa >= 7.0 and gpa < 8.0:
                return 3.0
            elif gpa >= 6.0 and gpa < 7.0:
                return 2.5
            elif gpa >= 5.5 and gpa < 6.0:
                return 2.0
            elif gpa >= 5.0 and gpa < 5.5:
                return 1.5
            elif gpa >= 4.0 and gpa < 5.0:
                return 1.0
            elif gpa >= 0 and gpa < 4.0:
                return 0
    except: 
        return 'Please enter a gpa score in 10-point scale'
        
