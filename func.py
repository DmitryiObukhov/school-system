class SchoolSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.subjects = []
        self.classes = []
        self.grades = []

    def add_student(self, student_id, name, enrollment_date):
        self.students.append({"id": student_id, "name": name, "enrollment_date": enrollment_date})

    def add_teacher(self, teacher_id, name, hire_date):
        self.teachers.append({"id": teacher_id, "name": name, "hire_date": hire_date})

    def add_subject(self, subject_id, name):
        self.subjects.append({"id": subject_id, "name": name})

    def add_class(self, class_id, name, time, subject_id, teacher_id):
        self.classes.append({"id": class_id, "name": name, "time": time, "subject_id": subject_id, "teacher_id": teacher_id})

    def add_grade(self, student_id, class_id, grade):
        self.grades.append({"student_id": student_id, "class_id": class_id, "grade": grade})

    def enroll_student_in_class(self, student_id, class_id):
        if any(student["id"] == student_id for student in self.students) and \
           any(class_info["id"] == class_id for class_info in self.classes):
            print(f"Student {student_id} enrolled in class {class_id}")
        else:
            print("Student or class not found.")

    def display_student_info(self, student_id):
        student_info = next((student for student in self.students if student["id"] == student_id), None)
        if student_info:
            print(f"Student ID: {student_info['id']}")
            print(f"Name: {student_info['name']}")
            print(f"Enrollment Date: {student_info['enrollment_date']}")
            print("Classes:")
            for grade_info in self.grades:
                if grade_info["student_id"] == student_id:
                    class_info = next(class_info for class_info in self.classes if class_info["id"] == grade_info["class_id"])
                    print(f"- Class ID: {class_info['id']}, Name: {class_info['name']}, Grade: {grade_info['grade']}")
        else:
            print("Student not found.")
