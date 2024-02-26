#********************************************************
#Program Name: Day9ExtraCredit.py
#Programmer: Alexander Struna
#Date: Feb 18, 2024
#Purpose: Write a program that adds up ten numbers (floats) entered by the users.  
#Input: input() a float 
#Output: print() the total of 10 numbers the user inputted 
#*************************************************
#This defines the function and helps keep track of the count of the loop and the total of the numbers entered
def main():
    total = 0.0
    count = 0
# This will start the loop that will repeat until the user enters 10 valid float numbers, and if they don't enter a valid flaot number, it will let them know it was wrong and to try again, but won't actually count the mistake as a full loop count due to the except section
    while count < 10:
        try:
            user_input = input("Enter a float number: ")
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("That wassn't a valid user input. Please enter a valid float number no characters allowed.")

    print("Total:", total)

if __name__ == "__main__":
    main()
