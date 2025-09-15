# print the first line
number = int(input("Enter a number: "))

# fizz if num is a multiple of 3, buzz if num is a multiple of 5, fizzbuzz if num is a multiple of 15, number if other cases 
# order of if-else: fizzbuzz -> fizz -> buzz
if number % 15 == 0:
  print("fizzbuzz")
elif number % 3 == 0:
  print("fizz")
elif number % 5 == 0:
  print("buzz")
else: 
  print(number)
