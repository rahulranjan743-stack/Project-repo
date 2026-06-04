import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = {}


def register_student():
    usn = input("Enter USN: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    students[usn] = {
        "Name": name,
        "Age": age,
        "Courses": [],
        "Marks": [],
        "Fee": 0
    }

    print("Student Registered Successfully")


def enroll_course():
    usn = input("Enter USN: ")

    if usn in students:
        n = int(input("How many courses? "))

        for i in range(n):
            course = input("Enter Course Name: ")
            students[usn]["Courses"].append(course)

        print("Courses Added Successfully")
    else:
        print("Student Not Found")


def evaluate_grade():
    usn = input("Enter USN: ")

    if usn in students:
        n = int(input("Enter number of subjects: "))
        marks = []

        for i in range(n):
            m = int(input(f"Enter marks for Subject {i+1}: "))
            marks.append(m)

        students[usn]["Marks"] = marks

        avg = sum(marks) / len(marks)

        if avg >= 90:
            grade = "A+"
        elif avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        print("Average Marks:", avg)
        print("Grade:", grade)
    else:
        print("Student Not Found")


def calculate_fee(course_count):
    fee_per_course = 5000
    return course_count * fee_per_course


def assign_fee():
    usn = input("Enter USN: ")

    if usn in students:
        count = len(students[usn]["Courses"])
        total_fee = calculate_fee(count)

        students[usn]["Fee"] = total_fee

        print("Total Fee =", total_fee)
    else:
        print("Student Not Found")


def display_students():
    if not students:
        print("No Records Found")
        return

    for usn, data in students.items():
        print("\nUSN:", usn)
        print("Name:", data["Name"])
        print("Age:", data["Age"])
        print("Courses:", data["Courses"])
        print("Marks:", data["Marks"])
        print("Fee:", data["Fee"])


def search_student():
    key = input("Enter USN to Search: ")

    if key in students:
        print(students[key])
    else:
        print("Student Not Found")


def sort_students():
    sorted_data = sorted(
        students.items(),
        key=lambda x: x[1]["Name"]
    )

    print("\nStudents Sorted by Name")

    for usn, data in sorted_data:
        print(usn, data["Name"])


def save_records():
    with open("students.json", "w") as file:
        json.dump(students, file)

    print("Records Saved to File")


def load_records():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        print("Records Loaded Successfully")

    except FileNotFoundError:
        print("File Not Found")


def scan_directory():
    path = input("Enter Directory Path: ")

    try:
        files = os.listdir(path)

        print("Files in Directory:")

        for f in files:
            print(f)

    except FileNotFoundError:
        print("Directory Not Found")

    except PermissionError:
        print("Permission Denied")


def analytics():
    if not students:
        print("No Data Available")
        return

    rows = []

    for usn, data in students.items():
        marks = data.get("Marks", []) or []

        if marks:
            avg = float(np.mean(marks))
            count = len(marks)
        else:
            avg = 0.0
            count = 0

        rows.append({
            "USN": usn,
            "Student": data.get("Name", ""),
            "Average": avg,
            "MarksCount": count
        })

    df = pd.DataFrame(rows)

    print("\nStudent Performance Data (all students)")
    print(df[["USN", "Student", "MarksCount", "Average"]])

    if df["MarksCount"].sum() > 0:
        class_avg = df[df["MarksCount"] > 0]["Average"].mean()
        median = df[df["MarksCount"] > 0]["Average"].median()

        top = df[df["MarksCount"] > 0].sort_values(
            "Average",
            ascending=False
        ).head(1)

        bottom = df[df["MarksCount"] > 0].sort_values(
            "Average"
        ).head(1)

        print(f"\nClass Average (students with marks): {class_avg:.2f}")
        print(f"Median Average: {median:.2f}")
        print(
            "Top Student:",
            top[["Student", "Average"]].to_dict("records")
        )
        print(
            "Bottom Student:",
            bottom[["Student", "Average"]].to_dict("records")
        )

    else:
        print("\nNo marks entered for any student. Averages shown as 0.0")

    plt.figure(figsize=(10, 6))
    plt.bar(df["Student"], df["Average"], color="skyblue")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Student Performance Analysis (All Students)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
        print("1. Register Student")
        print("2. Enroll Course")
        print("3. Grade Evaluation")
        print("4. Fee Calculation")
        print("5. Display Students")
        print("6. Search Student")
        print("7. Sort Students")
        print("8. Save Records")
        print("9. Load Records")
        print("10. Scan Directory")
        print("11. Student Analytics")
        print("12. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            register_student()

        elif choice == 2:
            enroll_course()

        elif choice == 3:
            evaluate_grade()

        elif choice == 4:
            assign_fee()

        elif choice == 5:
            display_students()

        elif choice == 6:
            search_student()

        elif choice == 7:
            sort_students()

        elif choice == 8:
            save_records()

        elif choice == 9:
            load_records()

        elif choice == 10:
            scan_directory()

        elif choice == 11:
            analytics()

        elif choice == 12:
            print("Exiting Program")
            break

        else:
            print("Invalid Choice")


main()
