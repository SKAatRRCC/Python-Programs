#********************************************************
#Program Name:          616Lab.py
#Programmer:     Alexander Struna
#Date:        Feb 10, 2024
#Purpose:      Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.
#Modules used:          None
#Input Variable(s):       int, input
def main():
    # Have the User input the name of the month and day 
    input_month = input("Enter the month: ")
    input_day = int(input("Enter the day: "))

    # Check if the month and day is valid
    if not is_valid_month(input_month):
        print("Invalid month")
        return
    if not (1 <= input_day <= 31):
        print("Invalid day")
        return

    # This line will help determine the season
    season = determine_season(input_month, input_day)
    if season:
        print(season)
    else:
        print("Invalid date")

def determine_season(month, day):
    # This sections helps defines the start and end dates for each season
    spring_start = (3, 20)
    spring_end = (6, 20)
    summer_start = (6, 21)
    summer_end = (9, 21)
    autumn_start = (9, 22)
    autumn_end = (12, 20)
    winter_start = (12, 21)
    winter_end = (3, 19)

    # This will back check the date  inputted against the defined ranges for each season
    if spring_start <= (get_month_number(month.lower()), day) <= spring_end:
        return "Spring"
    elif summer_start <= (get_month_number(month.lower()), day) <= summer_end:
        return "Summer"
    elif autumn_start <= (get_month_number(month.lower()), day) <= autumn_end:
        return "Autumn"
    elif winter_start <= (get_month_number(month.lower()), day) <= winter_end:
        return "Winter"
    else:
        return None

def is_valid_month(month):
    return month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

def get_month_number(month):
    # This will take the month entered and convert the month's name to a month's number
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
                  'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    return month_dict[month]

# Call the main function if the script is run
if __name__ == "__main__":
    main()
