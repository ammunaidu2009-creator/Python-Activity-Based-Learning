# Manufacturing Quality Control Matrix
threshold = 5.0
products = int(input("Enter number of products: "))
for i in range(products):
    name = input("\nEnter product name: ")
    batches = int(input("Enter number of batches: "))
    for j in range(batches):
        print("\nBatch", j + 1)
        production = int(input("Enter production quantity: "))
        defective = int(input("Enter defective units: "))
        if production <= 0 or defective < 0 or defective > production:
            print("Invalid production details")
            continue
        percentage = (defective / production) * 100
        print("Defect Percentage:", round(percentage, 2), "%")
        if percentage > threshold:
            print("Status: Quality Threshold Exceeded")
        else:
            print("Status: Quality Accepted")
print("\nQuality Control Analysis Completed")

