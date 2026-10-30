courses = [
    ("Python", 40),
    ("Maths", 30),
    ("Physics", 50)
]

rooms = [
    ("Room A", 35),
    ("Room B", 50)
]

periods = ["9 AM", "10 AM", "11 AM"]

timetable = []
allocated = 0

for course, students in courses:
    found = False

    for room, capacity in rooms:
        if capacity >= students:
            for period in periods:
                clash = False

                for entry in timetable:
                    if entry[1] == room and entry[2] == period:
                        clash = True

                if not clash:
                    timetable.append((course, room, period))
                    print(course, "->", room, "at", period)
                    allocated += 1
                    found = True
                    break

            if found:
                break

    if not found:
        print(course, "cannot be allocated!")

print("\n--- Final Timetable ---")
for course, room, period in timetable:
    print(course, "-", room, "-", period)

print("\nCourses:", len(courses))
print("Allocated:", allocated)

if allocated == len(courses):
    print("All courses allocated successfully!")
else:
    print("Some courses could not be allocated.")

