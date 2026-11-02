n = int(input("Enter number of routes: "))
routes = []
for i in range(n):
    print("\nRoute", i + 1)
    days = int(input("Enter number of days: "))
    passengers = 0
    time = 0
    fuel = 0
    for d in range(days):
        print("Day", d + 1)
        passengers += int(input("Enter passengers: "))
        time += float(input("Enter journey time: "))
        fuel += float(input("Enter fuel used: "))
    capacity = int(input("Enter bus capacity: "))
    efficiency = passengers / fuel if fuel > 0 else 0
    routes.append([i + 1, passengers, time,
                   fuel, capacity, efficiency])
print("\n--- ROUTE PERFORMANCE ---")
for r in routes:
    print("\nRoute:", r[0])
    print("Total Passengers:", r[1])
    print("Journey Time:", r[2])
    print("Fuel Used:", r[3])
    print("Efficiency:", round(r[5], 2))
    if r[1] > r[4] * days:
        print("Status: Overloaded")
    else:
        print("Status: Normal")
best = max(routes, key=lambda x: x[5])
print("\nMost Fuel Efficient Route:", best[0])

