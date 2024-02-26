#********************************************************
#Program Name: MondayextraCredit.py
#Programmer: Alexander Struna
#Date: Feb 19, 2024
#Purpose:Using a for-loop, write a program that finds all positive numbers that are evenly divisible by 10 and less then n (where n is an input from the user).
# Modules used: None
# Input Variable(s): int(input())
# Output: Numbers divisible by 10 from 0 to n-1
# ********************************************************

#this line is just defining the function then then having the user enter a value for n, so then that is the value of the variable n.
def main():
    # Get user input for the value of n
    n = int(input("Enter a whole number value for n: "))

    #this line initiates the forloop that executes the block of code repeatedly, and during each execution,
    #then the variable 'num' will take on the values from 0 to n-1.
    for num in range(n):
        # this will check if the number is evenly divisible by 10 becauyse the % operator is calculating the remainder after the division is finished, and then if the previous line is true, then it prents the statement on the same line.
        if num % 10 == 0:
            print(num, end=' ')

if __name__ == "__main__":
    main()
