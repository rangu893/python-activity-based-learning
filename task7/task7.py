rooms = [
    ["Room 101", 1, 120, 500],
    ["Room 102", 1, 180, 700],
    ["Room 201", 2, 250, 900],
    ["Room 202", 2, 100, 400]
]

electricity_rate = 8
water_rate = 2
electricity_limit = 200
water_limit = 600

floor_usage = {}

for room in rooms:
    name = room[0]
    floor = room[1]
    electricity = room[2]
    water = room[3]

    electricity_charge = electricity * electricity_rate
    water_charge = water * water_rate
    total_charge = electricity_charge + water_charge

    print("\nRoom:", name)
    print("Electricity:", electricity, "units")
    print("Water:", water, "litres")
    print("Total Charge: Rs.", total_charge)

    if electricity > electricity_limit:
        print("Warning: High electricity consumption")

    if water > water_limit:
        print("Warning: High water consumption")

    if floor not in floor_usage:
        floor_usage[floor] = [0, 0]

    floor_usage[floor][0] += electricity
    floor_usage[floor][1] += water

print("\n--- Floor-wise Resource Usage ---")

for floor, usage in floor_usage.items():
    print("Floor:", floor)
    print("Electricity:", usage[0], "units")
    print("Water:", usage[1], "litres")

print("\nMonitoring Completed.")

