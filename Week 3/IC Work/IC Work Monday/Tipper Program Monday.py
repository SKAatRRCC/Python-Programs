#29 Jan 2024 IC Assignment
#Tipper Program
#SKA

def main():
    # This line has the user enter the total from the resteraunt
    bill = float(input("Enter the restaurant bill total: $"))

    # This line is calculating the a 20% tip based on the bill
    tip_percentage = 0.20
    tip_amount = bill * tip_percentage
     # This line is printing/displaying the bill total, tip amount, and total bill amount and it is only to the second place as a dollar amount would be.

    print("Bill: ${:.2f}".format(bill))
    print("Tip: ${:.2f}".format(tip_amount))
    print("Total Amount: ${:.2f}".format(bill + tip_amount))

if __name__ == "__main__":
    main()
