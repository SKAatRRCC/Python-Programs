#********************************************************
#Program Name: HWproblem1.py
#Programmer: Alexander Struna
#Date: Feb 16, 2024
#Purpose: To Write a program with a loop that computes the sum of all the squares between 1 and 15 (inclusive – meaning include 15). This means square each number starting at 1 and going to 15 and add all these squared numbers togethe.
#Example: 1 * 1 + 2 * 2 + 3 * 3 + 4 * 4 and so on to 15 * 15.
#Input counter, and total
#Output: The sum of the squares from 1 to 15 is: 1240
#*************************************************

def main():
    counter = 0  # Start with the first number
    total = 0  # Initialize the total sum
#this will keep the loop going until the counter reaches 15, after each count it then it will add the square of the current number to the total, then finally the counter will increase by 1, and it will restart until it hits 15
    while counter <= 15:  
        total = total + counter ** 2  
        counter = counter + 1  

    print(f"The sum of the squares from 1 to 15 is: {total}")

if __name__ == "__main__":
    main()
