# task: find days of the week on a given date
def daysOfWeek(day, month, year):
    # 4 main formulas for calculating the day_of_week
    y0 = year - (14 - month) // 12
    x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    day_of_week = (day + x0 + 31 * m0 // 12) % 7
    
    # if-else code 
    if day_of_week == 0:
        return 'Sunday'
    elif day_of_week == 1:
        return 'Monday'
    elif day_of_week == 2:
        return 'Tuesday'
    elif day_of_week == 3:
        return 'Wednesday'
    elif day_of_week == 4:
        return 'Thursday'
    elif day_of_week == 5:
        return 'Friday'
    elif day_of_week == 6:
        return 'Saturday'
