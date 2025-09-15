# printing the first line
day = int(input("Enter number of days: "))

# formula for number of weeks
week = int(day / 7)

# days remain
remained_days = day - week * 7

# printing the second line
print(f"{day} days is {week} weeks plus {remained_days} days")
