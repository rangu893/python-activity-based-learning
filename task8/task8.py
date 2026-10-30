branches = {
    "Branch A": 50,
    "Branch B": 20,
    "Branch C": 10
}

target_stock = 30

surplus = {}
shortage = {}

# Find surplus and shortage
for branch, stock in branches.items():
    if stock > target_stock:
        surplus[branch] = stock - target_stock
    elif stock < target_stock:
        shortage[branch] = target_stock - stock

print("Surplus Stock:", surplus)
print("Shortage Stock:", shortage)

# Generate stock transfers
print("\n--- Transfer Plan ---")

for receiver in list(shortage.keys()):
    for sender in list(surplus.keys()):
        if shortage[receiver] > 0 and surplus[sender] > 0:
            quantity = min(shortage[receiver], surplus[sender])

            print(sender, "->", receiver, ":", quantity, "items")

            shortage[receiver] -= quantity
            surplus[sender] -= quantity

print("\n--- Remaining Shortages ---")
print(shortage)

print("\n--- Remaining Surplus ---")
print(surplus)

