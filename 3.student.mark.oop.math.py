from lab1b import input_courses, input_students, list_course, list_student, marks, marks_list
import os
import pickle
import gzip


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

        save_data(students, courses, student_marks)

        print("Data compressed and saved to students.dat.")

    list_student(students)
    list_course(courses)
    marks_list(student_marks, students, courses)

    print("\nSTUDENT LIST SORTED BY GPA (DESCENDING)")

    sorted_students = sort_students_by_gpa(students, student_marks)

    for index, student in enumerate(sorted_students, start=1):

        gpa = calculate_gpa(student["id"], student_marks)

        gpa_display = f"{gpa:.2f}" if gpa is not None else "N/A"

        print(f"{index}. ID: {student['id']}, "f"Name: {student['name']}, "f"Dob: {student['dob']}, "f"GPA: {gpa_display}")


if __name__ == "__main__":
    main()