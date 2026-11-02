n = int(input("Enter number of households: "))
fixed_fee = 50
for i in range(n):
    print("\nHousehold", i + 1)
    name = input("Enter household name: ")
    units = int(input("Enter water consumption: "))
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill += fixed_fee
    if units > 200:
        bill += 100
    print("\nHousehold:", name)
    print("Consumption:", units, "units")
    print("Total Water Bill: Rs.", bill)
    if units > 200:
        print("Status: Excessive Usage")
    else:
        print("Status: Normal Usage")

