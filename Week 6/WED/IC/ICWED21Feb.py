#********************************************************
#Program Name: ICWED21Feb.py
#Programmer: Alexander Struna
#Date: Feb 21, 2024
#Purpose:Write a function that calculates and returns the area of a rectangle 
#Modules used: None
#Input Variable(s): floats as base and height.
#Output: Out put are the print statements and the calculation of a rectangle based on the user inputs of b*h, and also will repeat doing so as long as user wants to continue. 
#********************************************************

#this defines the funcation and it will calculate the area of a rectangle 
def rectangle_area(base, height):
    return base * height

#this defines the next function and loops the try for a float until a valid ffloat is entered and then if the user entered something that won't work then it will have the user try their inputs again.
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That was an invalid input, please enter a numerical digit.")
#this will use the while loop to keep getting and calculating inputs as long as the user continues to say yes after inputing their valid float inputs, and the program outputting a calculation. if the user says no then the program finishes.
def main():
    while True:
        base = get_float_input("Enter the base of the rectangle: ")
        height = get_float_input("Enter the height of the rectangle: ")

        area = rectangle_area(base, height)
        print(f"The area of the rectangle is: {area}")

        repeat = input("Do you want to calculate the area of another rectangle? (YES or NO): ")
        if repeat != 'YES':
            break

if __name__ == "__main__":
    main()
