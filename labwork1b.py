def input_students():
    students = []
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"Student{i+1}")
        id = int(input("Enter ID: "))
        name = str(input("Enter name: "))
        dob = int(input("Enter day of birth: "))
        students.append({"id" : id ,"name" : name , "dob" : dob})
    return students

def input_courses():
    courses = []
    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"Course{i+1}")
        id = int(input("Enter ID: "))
        name = str(input("Enter name: "))
        courses.append({"id" : id ,"name" : name})
    return courses

def list_student(students):
    print("STUDENT LIST\n")
    for i,s in enumerate(students):
        print(f"{i+1}.ID : {s['id']}, Name: {s['name']}, Dob: {s['dob']}")

def list_course(courses):
    print("COURSE LIST\n")
    for i,s in enumerate(courses):
        print(f"{i+1}.ID : {s['id']}, Name: {s['name']}")

def marks(students, courses):
    marks = []
    for i in range(len(courses)):
        print(f"***Marks for course {courses[i]['name']}:")
        for j in range(len(students)):
            mark = float(input(f"Enter mark for student {students[j]['name']}: "))
            marks.append({"student_id": students[j]["id"], "course_id": courses[i]["id"], "mark": mark})
    return marks

def marks_list(marks, students, courses):
    print("MARKS LIST\n")
    for i in range(len(courses)):
        print(f"Course: {courses[i]['name']}")
        for j in range(len(students)):
            mark = next((m["mark"] for m in marks if m["student_id"] == students[j]["id"] and m["course_id"] == courses[i]["id"]), None)
            print(f"Student: {students[j]['name']}, Mark: {mark}")

def main():
    students = input_students()
    courses = input_courses()
    list_student(students)
    list_course(courses)
    student_marks = marks(students, courses)
    marks_list(student_marks, students, courses)


if __name__ == "__main__":
    main()
