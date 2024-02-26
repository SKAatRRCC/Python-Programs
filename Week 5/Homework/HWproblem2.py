#********************************************************
#Program Name: HWproblem2.py
#Programmer: Alexander Struna
#Date: Feb 18, 2024
#Purpose: Write a program that will find the largest number. 
#Input: input()
#Output: print()
#*************************************************

#this will start the total at 0 and defines the funcation and then assigns a variable to control the loops and to make sure it keeps looping/continuing as long as that input is true
def main():
    total = 0  
    
    continue_input = True 
    while continue_input:
    #below this section we're having the user input a positive floating number and then tells them to use N if they want the loop to stop, and then it will convert the input to a floating point number and assign it to the number variable.
        try:
            user_input = input("Enter a positive floating point number (and enter the letter N to stop): ")

            if user_input.upper() == 'N':
                continue_input = False  # Set the flag to exit the loop
            else:
                number = float(user_input)

                # This will make it check if the number inputted by the user is larger than the current total
                if number > total:
                    total = number
                    print(f"Largest number so far: {total}")
        #this will let the user know they caused an error by not putting in a correct floating point number, and has them input a correction
        except ValueError:
            print("Invalid input. Please enter a valid positive floating point number.")
            
    #once the loop finishes then this section will check that the start total is greater than 0, and if it's true then it will print, if it is false it will print that no valid numbers were entered
    if total != 0:
        print(f"The largest number entered is: {total}")
    else:
        print("No valid numbers were entered.")

if __name__ == "__main__":
    main()
