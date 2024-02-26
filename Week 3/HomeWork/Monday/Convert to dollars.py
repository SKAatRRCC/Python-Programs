#Week 3 Day 4 HW
#Convert to dollars
#SKA

# This gets the values from the user
nickels = int(input('enter the amount of nickles'))
dimes = int(input('enter the amount of dimes'))
quarters = int(input('enter the amount of quarters'))

# This will calculate all of the coins to a total amount in dollars and cents and print it to the nearest cent.
total_coins = (nickels * 5) + (dimes * 10) + (quarters * 25)
dollars = total_coins / 100.0
print(f'Amount: ${dollars:.2f}')
