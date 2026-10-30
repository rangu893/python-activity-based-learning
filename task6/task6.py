

wards = [
    ["General", 20, 15, 5, 3],
    ["Emergency", 10, 10, 2, 4],
    ["ICU", 8, 6, 1, 3]
]

# Format: [Ward, Total Beds, Occupied Beds, Available Staff, Equipment Needed]

for ward in wards:
    name = ward[0]
    total_beds = ward[1]
    occupied_beds = ward[2]
    staff = ward[3]
    equipment_needed = ward[4]

    available_beds = total_beds - occupied_beds

    print("\nWard:", name)
    print("Available Beds:", available_beds)
    print("Available Staff:", staff)

    if available_beds <= 2 or staff <= 1:
        print("Priority: HIGH")
    else:
        print("Priority: NORMAL")

    if available_beds <= 2:
        print("Shortage: Beds")

    if staff <= 1:
        print("Shortage: Staff")

    if equipment_needed > 3:
        print("Shortage: Equipment")

print("\nHospital Resource Report Completed.")
