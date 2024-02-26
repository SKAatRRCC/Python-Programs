#Week 1 Day 4 HW
#Calorie Calculator
#Formulas: ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781 - 75.4991) * time / 8.368
#SKA

# This line gets all the required inputs from the user for the calorie calculator 
age = int(input("Enter age in years: "))
weight = float(input("Enter weight in pounds: "))
heart_rate = int(input("Enter heart rate in beats per minute(BPM): "))
time = float(input("Enter exercise time in minutes: "))

# This line calculates calories burned based off the user input using the provided formula then prints the calories you have or will burn
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781 - 75.4991)) * time / 8.368
print(str(calories) + ' calories')

