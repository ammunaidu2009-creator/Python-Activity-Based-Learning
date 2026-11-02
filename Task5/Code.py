n = int(input("Enter number of branches: "))
branches = []
for i in range(n):
    print("\nBranch", i + 1)
    stock = int(input("Enter current stock: "))
    target = int(input("Enter target stock: "))
    branches.append([stock, target])
limit = int(input("\nEnter maximum transfer quantity: "))
surplus = []
shortage = []
for i in range(n):
    diff = branches[i][0] - branches[i][1]

    if diff > 0:
        surplus.append([i + 1, diff])
    elif diff < 0:
        shortage.append([i + 1, -diff])
print("\n--- STOCK TRANSFERS ---")
for s in surplus:
    for d in shortage:
        if s[1] > 0 and d[1] > 0:
            qty = min(s[1], d[1], limit)
            if qty > 0:
                print("Branch", s[0], "to Branch",
                      d[0], ":", qty, "units")
                s[1] -= qty
                d[1] -= qty
print("\n--- FINAL STOCK STATUS ---")
for i in range(n):
    print("Branch", i + 1,
          "Stock:", branches[i][0])

