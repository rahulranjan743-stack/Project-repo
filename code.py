import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Core runtime heap space
students = []
FILE_NAME = "students.csv"


def calculate_grade(cgpa):
    """Evaluates strict academic tier letter matching
    using clean boundary constraints."""
    
    if cgpa >= 9.0:
        return "A+"
    elif cgpa >= 8.0:
        return "A"
    elif cgpa >= 7.0:
        return "B"
    elif cgpa >= 6.0:
        return "C"

    return "D"


def calculate_eco_score(transport_mode):
    """Maps transport modes to specific corporate
    sustainability points."""
    
    scores = {
        "walking": 1,
        "bus": 3,
        "bike": 6,
        "car": 10
    }

    return scores.get(transport_mode.lower(), 5)


def calculate_fees(transport_mode):
    """Calculates final fee margins factoring in
    carbon footprints."""

    base_tuition = 300000

    # Apply standard zero/low-carbon footprint
    # model scholarship reduction

    eco_scholarship = (
        3000
        if calculate_eco_score(transport_mode) <= 3
        else 0
    )

    return base_tuition - eco_scholarship


def register_student():
    """Validates inputs and records a student profile
    to runtime memory."""

    print("\n--- Student Registration Pipeline ---")

    sid = input("ID: ").strip()

    # Prevents primary identifier collision
    if any(s['ID'] == sid for s in students):
        print("Error: Student ID already exists in system memory.")
        return

    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    sem = input("Semester: ").strip()

    try:
        cgpa = float(input("CGPA: "))

        if not (0.0 <= cgpa <= 10.0):
            print(
                "Invalid range constraint: "
                "CGPA must be inside 0.0 - 10.0 scale."
            )
            return

    except ValueError:
        print(
            "Type Exception: Numeric float scale "
            "expected for CGPA."
        )
        return

    transport = input(
        "Transport (walking/bus/bike/car): "
    ).strip().lower()

    courses_input = input(
        "Courses (comma-separated): "
    )

    courses = [
        c.strip()
        for c in courses_input.split(",")
        if c.strip()
    ]

    student_data = {
        "ID": sid,
        "Name": name,
        "Department": dept,
        "Semester": sem,
        "CGPA": cgpa,
        "Grade": calculate_grade(cgpa),
        "Transport": transport.capitalize(),
        "EcoScore": calculate_eco_score(transport),
        "Fee": calculate_fees(transport),
        "Courses": ", ".join(courses)
    }

    students.append(student_data)

    print(
        f"System: Registration complete for "
        f"student '{name}'."
    )


def save_records():
    """Safely commits runtime state arrays onto flat
    CSV databases."""

    if not students:
        print(
            "Warning: Memory buffer is empty. "
            "Registers are clear."
        )
        return

    try:
        fieldnames = [
            "ID",
            "Name",
            "Department",
            "Semester",
            "CGPA",
            "Grade",
            "Transport",
            "EcoScore",
            "Fee",
            "Courses"
        ]

        with open(
            FILE_NAME,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print(
            f"Success: Persistent data written "
            f"to file system space: '{FILE_NAME}'."
        )

    except IOError as e:
        print(
            f"I/O Storage Error: Failed to "
            f"execute system write: {e}"
        )


def load_records():
    """Automatically loads saved student files
    during initialization."""

    global students

    if os.path.exists(FILE_NAME):
        try:
            with open(
                FILE_NAME,
                "r",
                encoding="utf-8"
            ) as f:

                reader = csv.DictReader(f)

                students = []

                for row in reader:
                    row["CGPA"] = float(row["CGPA"])
                    row["EcoScore"] = int(row["EcoScore"])
                    students.append(row)

            print(
                f"Bootloader: Automated restoration "
                f"of {len(students)} records."
            )

        except Exception as e:
            print(
                f"Bootloader Exception: Failed "
                f"to decode repository: {e}"
            )


def search_student():
    """Performs quick linear lookup operations via
    distinct primary keys."""

    sid = input("Enter ID: ").strip()

    for s in students:
        if s["ID"] == sid:

            print("\n--- Structural Record Found ---")

            for key, val in s.items():
                print(f"{key:<12}: {val}")

            return

    print(
        "System Lookup: Specified reference "
        "identifier could not be matched."
    )


def sort_students_by_cgpa():
    """Orders students by highest academic
    performance indices."""

    if not students:
        print(
            "Data Error: Memory matrix contains "
            "zero instances to organize."
        )
        return

    sorted_set = sorted(
        students,
        key=lambda x: x["CGPA"],
        reverse=True
    )

    print(
        "\n--- Academic Merit Indexing "
        "(Descending Rank) ---"
    )

    for item in sorted_set:
        print(
            f"{item['Name']:<20} | "
            f"CGPA: {item['CGPA']:.2f} "
            f"[{item['Grade']}]"
        )


def scan_directory():
    """Safely inspects project directory structures,
    catching authorization anomalies."""

    folder = input("Folder name: ").strip()

    try:
        files = os.listdir(folder)

        print(
            f"\nWorkspace Structure for "
            f"'{folder}':"
        )

        for file in files:
            print(f"-> {file}")

    except FileNotFoundError:
        print(
            "Runtime Error: Target file path "
            "directory does not exist."
        )

    except PermissionError:
        print(
            "Security Error: Insufficient "
            "privilege access for path execution."
        )

    except Exception as e:
        print(
            f"System Exception: Directory "
            f"resolution failure: {e}"
        )


def generate_analytics():
    """Leverages NumPy and Pandas arrays to output
    system metric distributions."""

    if (
        not os.path.exists(FILE_NAME)
        or os.stat(FILE_NAME).st_size == 0
    ):
        print(
            "Analytics Flag: File stream "
            "uninitialized. Please save records first."
        )
        return

    try:
        df = pd.read_csv(FILE_NAME)

        print(
            "\n--- Structural Frame Ingest "
            "(Pandas Matrix Data) ---"
        )

        print(df.to_string(index=False))

        avg_cgpa = np.mean(df["CGPA"])

        print(
            f"Calculated Average Institutional "
            f"CGPA Matrix: {avg_cgpa:.2f}"
        )

        plt.figure(figsize=(6, 4))

        plt.hist(
            df["CGPA"],
            bins=5,
            color="teal",
            edgecolor="black",
            alpha=0.7
        )

        plt.xlabel("CGPA Value Range")
        plt.ylabel("Frequency Headcount")
        plt.title(
            "Academic Performance Threshold Distribution"
        )

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(
            f"Scientific Stack Core Exception: "
            f"Analytical crash: {e}"
        )


def main():
    load_records()

    while True:
        print("\n" + "=" * 45)
        print(
            "SMART CAMPUS COMPREHENSIVE "
            "CONTROL DASHBOARD"
        )
        print("=" * 45)

        print("1. Register Academic Student Instance")
        print("2. Commit Memory States to Disk Database (CSV)")
        print("3. Match and Retrieve Profile via Unique Key")
        print("4. Reorder Performance Tables via CGPA Rank")
        print("5. Verify Workspace Directories & Safety Scan")
        print("6. Run Numerical Analysis and Distribution Charts")
        print("7. Shutdown Administrative Console Interface")

        print("=" * 45)

        ch = input(
            "System Input Choice: "
        ).strip()

        if ch == "1":
            register_student()

        elif ch == "2":
            save_records()

        elif ch == "3":
            search_student()

        elif ch == "4":
            sort_students_by_cgpa()

        elif ch == "5":
            scan_directory()

        elif ch == "6":
            generate_analytics()

        elif ch == "7":
            print(
                "Console shut down gracefully.\n"
                "Process terminated."
            )
            break

        else:
            print(
                "Validation Flag: Invalid command "
                "string code identifier entered."
            )


if __name__ == "__main__":
    main()