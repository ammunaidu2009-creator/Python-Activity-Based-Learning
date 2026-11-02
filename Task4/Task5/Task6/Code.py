import math
# Store coordinates as tuples
points = []
n = int(input("Enter number of points: "))
for i in range(n):
    x = float(input("Enter latitude: "))
    y = float(input("Enter longitude: "))
    points.append((x, y))
distances = []
# Calculate distances between successive points
for i in range(n - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distances.append(d)
    print("Distance between", points[i],
          "and", points[i + 1], "=", round(d, 2))
# Find longest segment
if distances:
    longest = max(distances)
    index = distances.index(longest)
    print("\nLongest Route Segment:")
    print(points[index], "to", points[index + 1])
    print("Longest Distance:", round(longest, 2))
else:
    print("At least two points are required.")

