# task: program to return a leap year or not.
try: 
  year = int(input("Enter a year: ")) # declare a year, must be integer and > 0
  if year <= 0:
    print("The number must be positive")
  else: 
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): # conditions to return a leap year
      print("YES")
    else: 
      print("NO")
# tip: use try-except 
except: 
  print("Enter an integer, please")
