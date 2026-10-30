participants = []
registration_fee = 500

n = int(input("Enter number of participants: "))

for i in range(n):
    name = input("Enter participant ID: ")

    if name in participants:
        print("Duplicate registration!")
    else:
        participants.append(name)
        print("Registration successful!")

sponsorship = int(input("\nEnter sponsorship amount: "))
expenses = int(input("Enter total expenses: "))

# Financial calculations
total_participants = len(participants)
total_fees = total_participants * registration_fee
total_income = total_fees + sponsorship
balance = total_income - expenses

# Final report
print("\n--- Festival Audit Report ---")
print("Registered Participants:", participants)
print("Total Participants:5", total_participants)
print("Registration Fees:", total_fees)
print("Sponsorship Contributions:", sponsorship)
print("Total Income:", total_income)
print("Total Expenses:", expenses)
print("Final Balance:", balance)

if balance > 0:
    print("Status: Profit")
elif balance < 0:
    print("Status: Loss")
else:
    print("Status: Balanced")

