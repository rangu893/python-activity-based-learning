seats = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

registered_ids = ["S101", "S102", "S103", "S104", "S105"]
entered_ids = []
capacity = 9

print("Campus Event Entry System")

ticket = input("Enter your ticket ID: ")

if ticket not in registered_ids:
    print("Invalid ticket!")
elif ticket in entered_ids:
    print("Duplicate entry detected!")
else:
    entered_ids.append(ticket)

    seat_number = len(entered_ids)
    print("Entry successful!")
    print("Your seat number:", seat_number)

print("\n--- Event Report ---")
print("Total Seating Capacity:", capacity)
print("Registered Students:", len(registered_ids))
print("Students Entered:", len(entered_ids))
print("Available Seats:", capacity - len(entered_ids))

print("\n--- Seating Arrangement ---")
for row in seats:
    print(row)

