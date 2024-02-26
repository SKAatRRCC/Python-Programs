#********************************************************
#Program Name: problem2MonDay10.py
#Programmer: Alexander Struna
#Date: Feb 19, 2024
#Purpose:Write a program that finds the range (difference between the smallest and largest) of 8 positive integer numbers the user inputs inside a “for loop” with a range().
#Modules used:None
#Input Variable(s): int(input())
#Output:  
#********************************************************


#this section defines my main function and then the while loop will keep the program going until it is stopped by the user. Then try line starts the section that's going to get inputs and check for input errors from the user. 
def main():
    while True:
        try:
            # This will initialize the variables to help keep track of the largest and smallest numbers since we're trying to find the range 
            largest = 0
            smallest = 0

            # Get the first input to set initial values for largest and smallest
            user_input = int(input("Enter a positive whole number: "))
            
            # This is my "if" test which will check if the entered number is positive or not, and if it's a int or a float then telling the program to move on to the next section
            if user_input <= 0:
                print("Enter a positive whole number:")
                continue

            # these lines just set the initial values for largest and smallest based off what the users input was/is
            largest = user_input
            smallest = user_input

            # this section is a for loop that will repeat 7 more times asking for the user iput, so it can get 7 additional inputs of whole numbers.
            for _ in range(1, 8):
                user_input = int(input("Enter a positive whole number: "))

                #this is an additional "if" test which will check if the entered number is positive or not, and if it's a int or a float then telling the program to move on to the next section
                if user_input <= 0:
                    print("That wasn't a postive whole number, please enter a positive whole number:")
                    continue

                # this is the same as earlier except instead of setting the initial values for the largest and smallest numbers, it updates it the variables based on the user inputs
                if user_input > largest:
                    largest = user_input
                elif user_input < smallest:
                    smallest = user_input

            # this section will calculate the range and print the value then it will ask if we want to repeat the program againm and will restart from step one if the user says YES and it will end if the user says NO
            range_value = largest - smallest
            print(f'The range is: {range_value}')

            repeat = input("Do you want to do this again? (YES/NO): ")
            if repeat != 'YES':
                break
        #this line will check/catch any invalid inputs from the user and tells the user to input a correct whole number. 
        except ValueError:
            print("Invalid input. Please enter a valid whole numerical digit/number.")

if __name__ == "__main__":
    main()
