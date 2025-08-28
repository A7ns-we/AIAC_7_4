class StudentRecord:
    def __init__(self, name, student_id, courseList=None):
        self.student_name = name
        self.student_id = student_id
        self.courses = courseList if courseList is not None else []

    def add_course(self, course):
        self.courses.append(course)

    def get_summary(self):
        return f"Student: {self.student_name}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def department_summary(self):
        return f"Department: {self.dept_name}, Total Students: {len(self.students)}"


# --- Usage Example ---
s1 = StudentRecord("Alice", 101, ["Math", "Science"])
d1 = Department("Computer Science")

d1.enroll_student(s1)

print(s1.get_summary())
print(d1.department_summary())
