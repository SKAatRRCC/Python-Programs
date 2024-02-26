#********************************************************
#Program Name: ICMonday19Feb.py
#Fun Program Name:"Dice Roller 3000"
#Programmer: Alexander Struna
#Date: Feb 19, 2024
#Purpose:Write a program that will throw a die six times using a "for loop" and then finds the total value of the six throws.
#Modules used: Random 
#Input Variable(s): None
#Output: The total of what a randomly generated number between 1-6 added up after it is thrown or rolled 6 times.
#********************************************************

#this import random line is uysing a random model and will generate random numbers for the program below
import random
#this will define the function and then sets the initial value of total to 0 to keep track of our dice rolls 
def main():
    total = 0
#this will cause the for loop to "roll" the dice 6 times, then define our dice 1-6, and for each time the loop is ran then a randomly generated number within the range we assigned will be added to the total and then once it's finished rolling 6 times it will print the statement and the total #
    for i in range(6):
        total += random.randint(1,6)
    print(f'Total value of six throws: {total}')
        	
if __name__ == "__main__":
    main()



