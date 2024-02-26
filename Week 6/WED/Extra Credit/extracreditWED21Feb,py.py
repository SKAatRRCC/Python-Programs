#********************************************************
#Program Name: extracreditWED21Feb.py
#Programmer: Alexander Struna
#Date: Feb 21, 2024
#Purpose:Input three numbers in main() and then write the following functions below outside of main().
#Modules used: None
#Input Variable(s): int(input()) for x, y, & z
#Output: the output depends on the user inputs, but it will be either All numbers are the same. different, or neither essentially. 
#********************************************************

#This line defines the function to check if all numbers are the same
def allTheSame(x, y, z):
    return x == y == z

#This line defines the function to check if all numbers are different
def allDifferent(x, y, z):
    return x != y and y != z and x != z

#This defines the main function and starts the while loop until the user kills the program by saying NO when prompted.
def main():
    while True:
        try:
            #this section gets the user to input three integers from the user
            x = int(input("Enter the first whole number: "))
            y = int(input("Enter the second whole number: "))
            z = int(input("Enter the third whole number: "))

            #this section call the 2 functions allthesame or alldifferent and print the results. if it's neither of them then the else section prints that they are not all the same or different.
            if allTheSame(x, y, z):
                print("All numbers are the same.")
            elif allDifferent(x, y, z):
                print("All numbers are different.")
            else:
                print("The inputted numbers are neither all the same or all different.")

            #this prompts the user to kill or repeat the program by inputting YES or NO.
            repeat = input("Do you want to run the program again? (YES/NO): ")
            if repeat != 'YES':
                break
#this will check to make sure the user didn't enter any letters, symbols, or floats 
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
