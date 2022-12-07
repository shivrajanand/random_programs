month = int(input("Enter the serial number of month: "))

if (month < 1) or (month > 12):
    print("Invalid month serial")

days31 = [1, 3, 5, 7, 8, 10, 12]

if month == 2:
    print("28 or 29 days")
elif month in days31:
    print("31 days")
else:
    print("30 days")
