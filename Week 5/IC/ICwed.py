#********************************************************
#Program Name: ICwed.py
#Programmer: Alexander Struna
#Date: Feb 14, 2024
#Purpose: To Write a program that will use a while loop to sum 5 floating point numbers. Only have one input() statement.
#Modules used: None
#Input Variable(s): float(),input(), try/except for whether the user correctly inputs a floating point number
#Output: Enter a floating point number:, Invalid input. Please enter a valid floating-point number., & The sum of the 5 numbers is: [sum_value]
#********************************************************


# This is the section that will use to define the main function
def main():
     
    # This is assigning the variables
    total_sum = 0.0
    count = 0

    # the below is a while loops that will repeatedly execute the below until the user inputs 5 valid inputs.
    while count < 5:
        try:
            # This line will have the user enter a floating point number, and takes the input and makes it into afloat
            user_input = float(input("Enter a floating point number: "))
            
            # This line just adds the entered number to the total sum
            total_sum += user_input
            
            # this line keeps track of the of the number of valid inputs by adding 1 to the count after it started initially at 0, so the loops checks it again until it reaches 5
            count += 1
        
        # this is to deal with any user error inputs, so if the user enters something other than a flaoting point number while the above is trying to execute that count it will give the below statement and ask you you enter a valid input then it will try again.
        except ValueError:
            print("Invalid input. Please enter a valid floating point number.")

    # Print the total sum of the 5 valid numbers
    print(f"The sum of the 5 numbers is: {total_sum}")

if __name__ == "__main__":
    main()
