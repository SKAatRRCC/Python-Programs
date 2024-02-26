#24Jan2023 WED Homework Problem 2
#Write a program that will calculate the cost of miles driven (when a user enters fuel efficiency and price per gallon).
#Then calculate the cost to drive the above miles.
#SKA

mpg_Highway = int(input("enter Highway MPG rating (fuel efficency) for your vehicle: "))
mpg_City = int(input("enter City MPG rating (fuel efficency) for your vehicle: "))
fuel_Price = float(input("enter the price of fuel per gallon to the nearest whole cent:" ))
city_Miles = float(input("enter the total city distance in miles to the nearest half mile: "))
highway_Miles = float(input("enter the total highway distance in miles to the nearest half mile: "))
total_Miles = city_Miles + highway_Miles
city_Cost= (city_Miles/mpg_City) * fuel_Price
highway_Cost= (highway_Miles/mpg_Highway) * fuel_Price
total_Cost= round(highway_Cost + city_Cost, 2)
print("The cost to drive", city_Miles, "miles through the city is: $", round(city_Cost, 2))
print("The cost to drive", highway_Miles, "miles on the highway is: $", round(highway_Cost, 2))
print("The cost to drive", total_Miles, "total miles through the city and highway is: $", total_Cost)
