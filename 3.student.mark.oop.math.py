from lab1b import input_courses, input_students, list_course, list_student, marks, marks_list
import os
import pickle
import gzip
import csv
import polars as pl



def calculate_gpa(student_id, student_marks):
    scores = [
        record["mark"]
        for record in student_marks
        if record["student_id"] == student_id
    ]

    if not scores:
        return None

    return sum(scores) / len(scores)


def sort_students_by_gpa(students, student_marks):
    return sorted(
        students,
        key=lambda student: (
            calculate_gpa(student["id"], student_marks) is not None,
            calculate_gpa(student["id"], student_marks) or 0,
        ),
        reverse=True,
    )


# =========================
# EX6: PICKLE + COMPRESSION
# =========================

def save_data(students, courses, student_marks):
    data = {
        "students": students,
        "courses": courses,
        "student_marks": student_marks
    }

    with gzip.open("students.dat", "wb") as f:
        pickle.dump(data, f)


def load_data():
    with gzip.open("students.dat", "rb") as f:
        data = pickle.load(f)

    return data["students"], data["courses"], data["student_marks"]


# =========================
# EXTRA: EXPORT CSV
# =========================

def export_csv(students, courses, student_marks):

    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

    with open("courses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=courses[0].keys())
        writer.writeheader()
        writer.writerows(courses)

    with open("marks.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=student_marks[0].keys())
        writer.writeheader()
        writer.writerows(student_marks)


# =========================
# EXTRA: POLARS
# =========================

def load_frames():

    students_df = pl.read_csv("students.csv")
    courses_df = pl.read_csv("courses.csv")
    marks_df = pl.read_csv("marks.csv")

    return students_df, courses_df, marks_df


# =========================
# EXTRA: QUERY
# =========================

def query_students(students_df):

    condition = input(
        'Enter condition (example: name = "Mr.Happy"): '
    )

    field, value = condition.split("=")

    field = field.strip()
    value = value.strip().strip('"').strip("'")

    result = students_df.filter(
        pl.col(field) == value
    )

    print(result)


# =========================
# MAIN
# =========================

def main():

    if os.path.exists("students.dat"):

        print("Loading data from students.dat...")

        students, courses, student_marks = load_data()

    else:

        print("students.dat not found.")
        print("Creating new data...")

        students = input_students()
        courses = input_courses()
        student_marks = marks(students, courses)

        save_data(
            students,
            courses,
            student_marks
        )

        print("Data compressed and saved to students.dat.")

    list_student(students)
    list_course(courses)
    marks_list(
        student_marks,
        students,
        courses
    )

    print("\nSTUDENT LIST SORTED BY GPA (DESCENDING)")

    sorted_students = sort_students_by_gpa(
        students,
        student_marks
    )

    for index, student in enumerate(
        sorted_students,
        start=1
    ):

        gpa = calculate_gpa(
            student["id"],
            student_marks
        )

        gpa_display = (
            f"{gpa:.2f}"
            if gpa is not None
            else "N/A"
        )

        print(
            f"{index}. "
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Dob: {student['dob']}, "
            f"GPA: {gpa_display}"
        )


if __name__ == "__main__":
    main() 