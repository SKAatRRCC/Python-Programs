#********************************************************
#Program Name: problem2WED21Feb.py
#Programmer: Alexander Struna
#Date: Feb 21, 2024
#Purpose:Write a program that has a main() and the following functions, where r is radius and h is the height
#Modules used: None
#Input Variable(s): float(input()) for r & h
#Output: The output is the Sphere Volume:, Sphere Surface Area: ,Cone Volume: , Cone Surface Area: calculated volumes and surface areas based on the user's inputted radius and height. 
#********************************************************

#this line defines the function to and formula to calculate the volume of a sphere
def sphereVolume(r):
    return (4 / 3) * 3.14 * r ** 3
#this line defines the function to and formula to calculate the surface area of a sphere
def sphereSurface(r):
    return 4 * 3.14 * r ** 2
#this line defines the function to and formula to calculate the volume of a cone
def coneVolume(r, h):
    return (1 / 3) * 3.14 * r ** 2 * h
#this line defines the function to and formula to calculate the surface area of a cone
def coneSurface(r, h):
    return 3.14 * r * (r + (r ** 2 + h ** 2) ** 0.5)

#this defines the main function that uses a while loop and the try gets the user inputs to define the varibles that will be used in calculating the sphere and cone volume and surface areas
def main():
    while True:
        try:
            #this section gets the user input for radius, r and height, h
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))

            #after we get the user input this section will call each function and print the results
            print(f"Sphere Volume: {sphereVolume(r):.2f}")
            print(f"Sphere Surface Area: {sphereSurface(r):.2f}")
            print(f"Cone Volume: {coneVolume(r, h):.2f}")
            print(f"Cone Surface Area: {coneSurface(r, h):.2f}")

            # This will s sk the user if they want to continue repeating the program or end it by saying YES or NO
            repeat = input("Do you want to calculate again? (YES/NO): ")
            if repeat != 'YES':
                break
#this section just checks for input errors and tells the user to fix it by putting in a valid numerical number. 
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
