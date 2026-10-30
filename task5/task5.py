locations = ["Warehouse", "Shop A", "Shop B"]

for location in locations:
    print("\nLocation:", location)

    received = int(input("Enter quantity received: "))
    distributed = int(input("Enter quantity distributed: "))
    damaged = int(input("Enter quantity damaged: "))
    expected = int(input("Enter expected remaining stock: "))
    target = int(input("Enter target stock: "))

    remaining = received - distributed - damaged
    discrepancy = expected - remaining
    replenishment = max(0, target - remaining)

    print("\n--- Stock Report ---")
    print("Location:", location)
    print("Calculated Remaining Stock:", remaining)
    print("Discrepancy:", discrepancy)

    if discrepancy == 0:
        print("Status: Stock matches")
    else:
        print("Status: Stock discrepancy found")

    print("Replenishment Required:", replenishment)

print("\nStock reconciliation completed.")

