#********************************************************
#Program Name:          stateofH2O.py
#Programmer:              Alexander Struna
#Date:                              Feb 10, 2024
#Purpose:         		A program that reads a letter of either C for Celsius or F for Fahrenheit and then inputs a temperature value for that C or F. Then determine if clear water at sea level is a liquid, solid, or gas.
#Modules used:              None
#Input Variable(s):           temperature_scale (str), temperature_value (float)
#Output:                            A print statement, that output the variable answer 
#				    as an integer. #********************************************************

def main():
    print("Clear Water State at Sea Level Program")
    # Have the user input if it's Celsius (C) or Fahrenheit (F) then determine the state of matter the H2O is in (at sea level)
    try:
        # Have the user input for temperature Either Celsius or Fahrenheit
        temperature_scale = input("Enter temperature scale (F for Fahrenheit, C for Celsius): ").upper()
        # Have the user input for temperature value
        temperature_value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
        return

    # Determine the state of H2O based on the conditions provided by the user
    if temperature_scale == 'F':
        if temperature_value <= 32:
            state = 'solid'
        elif temperature_value >= 212:
            state = 'gas'
        else:
            state = 'liquid'
    elif temperature_scale == 'C':
        if temperature_value <= 0:
            state = 'solid'
        elif temperature_value >= 100:
            state = 'gas'
        else:
            state = 'liquid'
    else:
        print("Invalid temperature scale. Please enter 'F' or 'C'.")
        return

    # Output the result
    print(f"At {temperature_value} degrees {temperature_scale}, clear water at sea level is in the {state} state.")

if __name__ == "__main__":
    main()
