#Week 3 Day 5 HW
#Phone number breakdown
#Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.
#SKA

# This will get the 10 digit phone number
phone_number = int(input('enter a 10 digit phone number, numbers only. : '))

# This will figure out the area code, prefix, and line number the output the phone number in the corrected format.
area_code = phone_number // 10000000
prefix = (phone_number % 10000000) // 10000
line_number = phone_number % 10000
print(f'({area_code}) {prefix}-{line_number}')
