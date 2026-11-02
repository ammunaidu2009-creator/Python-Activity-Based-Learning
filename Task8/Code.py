n = int(input("Enter number of incidents: "))
incidents = []
for i in range(n):
    print("\nIncident", i + 1)
    name = input("Enter incident name: ")
    severity = int(input("Enter severity (1-5): "))
    location = input("Enter location: ")
    frequency = int(input("Enter reported frequency: "))
    score = severity * 3 + frequency * 2
    incidents.append([name, location, score])
incidents.sort(key=lambda x: x[2], reverse=True)
print("\n--- PRIORITY SUMMARY ---")
for item in incidents:
    if item[2] >= 20:
        status = "High Priority"
    elif item[2] >= 12:
        status = "Medium Priority"
    else:
        status = "Low Priority"
    print("Incident:", item[0])
    print("Location:", item[1])
    print("Score:", item[2])
    print("Priority:", status)
    print()

