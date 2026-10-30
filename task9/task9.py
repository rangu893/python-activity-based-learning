records = []
n = int(input("Enter number of registrations: "))

for i in range(n):
    print("\nEnter registration in format: ID,Name,Email")
    data = input().strip()
    fields = data.split(",")

    if len(fields) != 3:
        print("Error: Invalid number of fields")
        continue

    sid, name, email = fields
    sid = sid.strip()
    name = name.strip()
    email = email.strip()

    if sid == "" or name == "" or email == "":
        print("Error: Empty field")

    elif len(sid) != 4:
        print("Error: ID must contain 4 characters")

    elif not name.replace(" ", "").isalpha():
        print("Error: Invalid name format")

    elif "@" not in email or "." not in email:
        print("Error: Invalid email format")

    elif sid in records:
        print("Error: Duplicate ID")

    else:
        records.append(sid)
        print("Registration successful!")
        print("ID:", sid)
        print("Name:", name)
        print("Email:", email)

print("\nTotal successful registrations:", len(records))
print("Registered IDs:", records)
