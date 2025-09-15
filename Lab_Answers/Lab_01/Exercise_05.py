# print the first line
number = int(input("Enter a number (from 0 to 999): "))

# find first digit
first_digit = int(number / 100)

# find the remain after first digit
remainder_after_first = number - first_digit * 100

# find second digit
second_digit = int(remainder_after_first / 10)

# find the remain after second digit
remainder_after_second = number - first_digit * 100 - second_digit * 10

# find third digit
third_digit = int(remainder_after_second)

# sum up all three digits
result = first_digit + second_digit + third_digit

# print the second line
print(f"The sum of digits is: {result}")
