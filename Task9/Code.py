students = []
events = []
resources = []
while True:
    print("\n--- SMART CAMPUS MANAGEMENT ---")
    print("1. Student Records")
    print("2. Attendance")
    print("3. Marks")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append([name, roll, 0, 0])
        print("Student added successfully")
    elif choice == 2:
        roll = input("Enter roll number: ")
        for s in students:
            if s[1] == roll:
                s[2] += 1
                print("Attendance recorded")
                break
        else:
            print("Student not found")
    elif choice == 3:
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks: "))
        for s in students:
            if s[1] == roll:
                s[3] = marks
                print("Marks updated")
                break
        else:
            print("Student not found")
    elif choice == 4:
        roll = input("Enter roll number: ")
        event = input("Enter event name: ")
        events.append((roll, event))
        print("Event registered")
    elif choice == 5:
        resource = input("Enter resource name: ")
        room = input("Enter allocated room: ")
        resources.append((resource, room))
        print("Resource allocated")
    elif choice == 6:
        print("\n--- CAMPUS SUMMARY ---")
        for s in students:
            name, roll, attendance, marks = s
            print("Name:", name)
            print("Roll No:", roll)
            print("Attendance:", attendance)
            print("Marks:", marks)
            if marks >= 40:
                print("Result: Pass")
            else:
                print("Result: Fail")
        print("\nEvent Registrations:", events)
        print("Resource Allocations:", resources)
        print("Total Students:", len(students))
    elif choice == 7:
        print("Exiting Campus Management")
        break
    else:
        print("Invalid choice")

