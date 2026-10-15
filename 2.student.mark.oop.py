class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    @staticmethod
    def input_students():
        students = []
        count = int(input("Enter number of students: "))

        for i in range(count):
            print(f"Student{i + 1}")
            student_id = int(input("Enter ID: "))
            name = input("Enter name: ")
            dob = int(input("Enter day of birth: "))

            students.append(Student(student_id, name, dob))

        return students

    @staticmethod
    def list_student(students):
        print("STUDENT LIST\n")
        for i, s in enumerate(students):
            print(f"{i + 1}.ID : {s.id}, Name: {s.name}, Dob: {s.dob}")


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    @staticmethod
    def input_courses():
        courses = []
        count = int(input("Enter number of courses: "))

        for i in range(count):
            print(f"Course{i + 1}")
            course_id = int(input("Enter ID: "))
            name = input("Enter name: ")

            courses.append(Course(course_id, name))

        return courses

    @staticmethod
    def list_course(courses):
        print("COURSE LIST\n")
        for i, c in enumerate(courses):
            print(f"{i + 1}.ID : {c.id}, Name: {c.name}")


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    @staticmethod
    def input_marks(students, courses):
        marks = []

        for course in courses:
            print(f"***Marks for course {course.name}:")
            for student in students:
                mark_value = float(
                    input(f"Enter mark for student {student.name}: ")
                )

                marks.append(
                    Mark(student.id, course.id, mark_value)
                )

        return marks

    @staticmethod
    def marks_list(marks, students, courses):
        print("MARKS LIST\n")

        for course in courses:
            print(f"Course: {course.name}")

            for student in students:
                mark_value = next(
                    (
                        m.mark for m in marks
                        if m.student_id == student.id
                        and m.course_id == course.id
                    ),
                    None
                )

                print(
                    f"Student: {student.name}, Mark: {mark_value}"
                )


def main():
    students = Student.input_students()
    courses = Course.input_courses()

    Student.list_student(students)
    Course.list_course(courses)

    student_marks = Mark.input_marks(students, courses)
    Mark.marks_list(student_marks, students, courses)


if __name__ == "__main__":
    main()
