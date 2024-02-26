#Week 3 Day 5 HW
#Simple Statistics
#SKA

# This will get 4 inputs from a user
num1 = float(input('enter value 1 to nearest decimal: '))
num2 = float(input('enter value 2 to nearest decimal: '))
num3 = float(input('enter value 3 to nearest decimal: '))
num4 = float(input('enter value 4 to nearest decimal: '))

# This will calculate the product and average of the inputs
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# This is an output with rounded integers then an output to three decimal places
print(f'{product:.0f} {round(average):.0f}')
print(f'{product:.3f} {average:.3f}')
