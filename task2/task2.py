  print("Passengers:", passengers)
    print("Buses Required:", buses)
    print("Total Bus Capacity:", total_capacity)
    print("Unserved Passengers:", unserved)
routes = ["Route A", "Route B", "Route C"]

bus_capacity = int(input("Enter bus capacity: "))

for route in routes:
    print("\n", route)
    passengers = int(input("Enter number of passengers: "))

    buses = passengers // bus_capacity

    if passengers % bus_capacity != 0:
        buses += 1

    total_capacity = buses * bus_capacity
    unserved = max(0, passengers - total_capacity)
print("\nTransport Allocation Completed!")
