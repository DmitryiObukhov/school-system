from classes.student import Student
from classes.teacher import Teacher
from classes.subject import Subject
from classes.classs import Class
from classes.grade import Grade
from classes.enrollment import Enrollment


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.subjects = []
        self.classes = []
        self.grades = []

    def add_student(self, student_id, name, enrollment_date):
        student = Student(student_id, name, enrollment_date)
        self.students.append(student)
        return student

    def add_teacher(self, teacher_id, name, hire_date):
        teacher = Teacher(teacher_id, name, hire_date)
        self.teachers.append(teacher)
        return teacher

    def add_subject(self, subject_id, name):
        subject = Subject(subject_id, name)
        self.subjects.append(subject)
        return subject

    def add_class(self, class_id, name, schedule, subject, teacher):
        class_obj = Class(class_id, name, schedule, subject, teacher)
        self.classes.append(class_obj)
        return class_obj

    def add_grade(self, student, class_obj, grade):
        grade_obj = Grade(student, class_obj, grade)
        self.grades.append(grade_obj)
        return grade_obj

    def enroll_student_in_class(self, student, class_obj):
        enrollment = Enrollment(student, class_obj)
        student.classes.append(enrollment)
        class_obj.students.append(enrollment)

    def display_student_info(self, student):
        print(f"Student ID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Enrollment Date: {student.enrollment_date}")
        print("Classes:")
        for enrollment in student.classes:
            class_obj = enrollment.class_obj
            grade = next((g.grade for g in self.grades if g.student == student and g.class_obj == class_obj), None)
            print(f"- Class ID: {class_obj.id}, Name: {class_obj.name}, Grade: {grade}")
