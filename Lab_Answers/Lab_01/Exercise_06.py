# print the first line
money = int(input("Enter an amount of money (divisible by 1000): "))

# find the 5000 VND coins
coins_five_thousand = int(money / 5000)

# find the remainder after 5000 VND coins
remainder_after_five = money - coins_five_thousand * 5000

# find the 2000 VND coins
coins_two_thousand = int(remainder_after_five / 2000)

# find the remainder after 2000 VND coins
remainder_after_two = money - coins_five_thousand * 5000 - coins_two_thousand * 2000

# find the 1000 VND coins
coins_one_thousand = int(remainder_after_two / 1000)

# print the second line
print(f"{money} = [ {coins_five_thousand} ]*5000 + [ {coins_two_thousand} ]*2000 + [ {coins_one_thousand} ]*1000")
