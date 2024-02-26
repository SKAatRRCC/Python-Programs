#Program Name:          inclassworkmon.py
#Programmer:              Alexander Struna
#Date:                              Feb 05, 2024
#Purpose:   Write a program that reads an integer. Then prints out if the integer is positive negative or zero. Make sure the person entering the number knows that they are to enter an integer and not a float (with a decimal).
#Modules used:              None
#Input Variable(s):         int


def main():
    # This will have the user input a whole number
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # This section will check if the number that the user entered is  either positive, negative, or zero
    if num > 0:
        print("The entered integer is positive.")
    elif num < 0:
        print("The entered integer is negative.")
    else:
        print("The entered integer is zero.")
if __name__ == "__main__":
    main()
