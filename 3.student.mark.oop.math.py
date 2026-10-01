from lab1b import input_courses, input_students, list_course, list_student, marks, marks_list


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


def main():
    students = input_students()
    courses = input_courses()
    list_student(students)
    list_course(courses)

    student_marks = marks(students, courses)
    marks_list(student_marks, students, courses)

    print("\nSTUDENT LIST SORTED BY GPA (DESCENDING)")
    for index, student in enumerate(
        sort_students_by_gpa(students, student_marks),
        start=1,
    ):
        gpa = calculate_gpa(student["id"], student_marks)
        gpa_display = f"{gpa:.2f}" if gpa is not None else "N/A"
        print(
            f"{index}. ID: {student['id']}, Name: {student['name']}, "
            f"Dob: {student['dob']}, GPA: {gpa_display}"
        )


if __name__ == "__main__":
    main()
