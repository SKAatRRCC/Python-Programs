#********************************************************
#Program Name: prob1WED21Feb.py
#Programmer: Alexander Struna
#Date: Feb 21, 2024
#Purpose:Write a program with three functions average3(…), smallest(…) and the main() function. Then in the main() function get input from the user, and then call these two functions (average3 & smallest), and print the results in main().
#Modules used: None
#Input Variable(s): float(input()
#Output: The output is the average 3 values inputted, and smallest of the 3 values inputted, and also asking if the user wants to repeat the program again or not
#********************************************************

#This defines the function and then has it calculate the average of three values by adding them together and dividing by 3
def average3(value1, value2, value3):
    return (value1 + value2 + value3) / 3

#This section defines the function to find the smallest of three values by utilizing the min function
def smallest(value1, value2, value3):
    return min(value1, value2, value3)

#This section defines the main function and the while loop keeps the program going until the user says to end it by responding NO
def main():
    while True:
        try:
            #this will have the user input 3 numerical values
            value1 = float(input("Enter the first numerical value: "))
            value2 = float(input("Enter the second numerical value: "))
            value3 = float(input("Enter the third numerical value: "))
            
            #this line causes the program to go back to the average3 function (call it) and store the result then moves down to the next line
            avg_result = average3(value1, value2, value3)
            
            #this line causes the program to go back to the smallest function (call it) and store the result then moves down to the print section
            smallest_result = smallest(value1, value2, value3)
            
            #this will print the average of the 3 values and the smallest of the 3 values
            print(f'The average of {value1}, {value2}, and {value3} is: {avg_result:.2f}')
            print(f'The smallest of {value1}, {value2}, and {value3} is: {smallest_result}')
            
            # this will have the user enter yes or no to either kill or cause the program to repeat, depending if the user inputs YES or NO.
            repeat = input("Do you want to try again? (YES/NO): ")
            if repeat != 'YES':
                break
            #this checks to make sure the user input an actual numerical value no a letter or symbol for example
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
