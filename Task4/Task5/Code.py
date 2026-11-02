# Traffic Flow and Congestion Analysis
roads = {}
n = int(input("Enter number of roads: "))
for i in range(n):
    name = input("\nEnter road name: ")
    capacity = int(input("Enter road capacity: "))
    counts = []
    for j in range(3):
        vehicles = int(input(f"Enter vehicles in time interval {j+1}: "))
        counts.append(vehicles)
    roads[name] = (capacity, counts)
print("\n--- Traffic Analysis Report ---")
for road, data in roads.items():
    capacity, counts = data
    total = sum(counts)
    peak = max(counts)
    peak_period = counts.index(peak) + 1
    if peak < 50:
        level = "Low"
    elif peak <= 100:
        level = "Medium"
    else:
        level = "High"
    print("\nRoad:", road)
    print("Total Vehicles:", total)
    print("Peak Traffic:", peak)
    print("Peak Period:", peak_period)
    print("Congestion Level:", level)
    if peak > capacity:
        print("Status: Exceeds Capacity")
    else:
        print("Status: Within Capacity")

