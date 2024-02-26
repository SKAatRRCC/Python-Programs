#********************************************************
#Program Name:          inclassworkwed.py
#Programmer:              Alexander Struna
#Date:                              Feb 07, 2024
#Purpose:         		A program that reads a letter of either C for Celsius or F for Fahrenheit and then inputs a temperature value for that C or F. Then determine if clear water at sea level is a liquid, solid, or gas.
#Modules used:              None
#Input Variable(s):           num, int
#Output:                            A print statement, that output the variable answer 
#				    as an integer. #********************************************************

def main():
    # This has the user input a number that's less than 1 billion
    num = int(input("Enter an integer (less than a billion): "))

    # This section will take the absolute value if the number is negative then initialize the digit count
    if num < 0:
        num = -num
    digits = 0

    # This section will check how many digits the number has
    if num < 10:
        digits = 1
    elif num < 100:
        digits = 2
    elif num < 1000:
        digits = 3
    elif num < 10000:
        digits = 4
    elif num < 100000:
        digits = 5
    elif num < 1000000:
        digits = 6
    elif num < 10000000:
        digits = 7
    elif num < 100000000:
        digits = 8
    elif num < 1000000000:
        digits = 9
    else:
        print("Number exceeds one billion. Please enter a smaller number.")
        return

    # This outputs the result
    print(f"The number {num} has {digits} digit(s).")


if __name__ == "__main__":
    main()
