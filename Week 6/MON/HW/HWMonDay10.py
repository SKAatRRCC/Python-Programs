#********************************************************
#Program Name: HWMonDay10.py
#Programmer: Alexander Struna
#Date: Feb 19, 2024
#Purpose:Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.
#Modules used:  
#Input Variable(s): int(input()),
#Output:  If the input is: -15, 10...the output is: -15 -10 -5 0 5 10 Ex: If the second integer is less than the first as in 20,5...the output is:Second integer can't be less than the first.
#********************************************************

#This section will define the function and then prompt the user to inpute a whole number two seperate times and then convert the input to an int(
def main():
    first_num = int(input("Enter the first whole number."))
    second_num = int(input("Enter the second whole number."))

#This section checks to make sure the user inputted a larger number than the first number they inputted. If they messed up then it notify's them , and asks them to fix it via trying again
    if second_num < first_num:
        print("Second whole number can't be less than the first whole number.")
        try_again = "yes"
#this just restarted the input question to after the user said yes to trying again, so they can fix their input mistake
        while try_again == "yes":
            first_num = int(input("Enter the first whole number."))
            second_num = int(input("Enter the second whole number."))
#this else is under the "if" section and checks if the statement " second_num < first_num:" is true or false, and if it's false then it skips that/moves on to the for line and then the for line starts a for loop than sets a range from the first number inputted and second number inputted in an increment of 5. (Also it doesn't matter if the input isn't a denomination of 5 as long as it isn't a float and is an int then everything will run properly)
    else:
        for num in range(first_num, second_num + 1, 5):
            print(num, end=" ")

        print()

if __name__ == "__main__":
    main()
