name = input("Enter student name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
prerequisite = input("Prerequisite completed? (yes/no): ")
print("\n--- Academic Audit Report ---")
print("Student Name:", name)
print("Marks:", marks)
print("Attendance:", attendance, "%")
if marks >= 40 and attendance >= 75 and prerequisite == "yes":
    print("Result: PASS")
    print("Eligible for next semester")
else:
    print("Result: NOT ELIGIBLE")

    if marks < 40:
        print("Requirement: Improve marks")
    if attendance < 75:
        print("Requirement: Improve attendance")
    if prerequisite != "yes":
        print("Requirement: Complete prerequisite")

