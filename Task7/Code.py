n = int(input("Enter number of participants: "))
participants = []
fee = float(input("Enter registration fee per person: "))
for i in range(n):
    name = input("Enter participant name: ")
    if name in participants:
        print("Duplicate registration:", name)
    else:
        participants.append(name)
sponsorship = float(input("Enter sponsorship amount: "))
expenses = float(input("Enter total expenses: "))
total_fee = len(participants) * fee
income = total_fee + sponsorship
balance = income - expenses
print("\n--- FESTIVAL FINANCIAL AUDIT ---")
print("Valid Participants:", participants)
print("Total Registrations:", len(participants))
print("Registration Income:", total_fee)
print("Sponsorship:", sponsorship)
print("Total Income:", income)
print("Total Expenses:", expenses)
print("Final Balance:", balance)

