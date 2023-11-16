from system import SchoolSystem
school_system = SchoolSystem()

math_subject = school_system.add_subject(1, 'Mathematics')
physics_teacher = school_system.add_teacher(1, 'John Doe', '2023-01-01')
class_10a = school_system.add_class(1, '10A', 'Mon, Wed, Fri 10:00-12:00', math_subject, physics_teacher)
student_ivanenko = school_system.add_student(1, 'John Ivanenko', '2023-01-01')

school_system.enroll_student_in_class(student_ivanenko, class_10a)
grade_ivanenko = school_system.add_grade(student_ivanenko, class_10a, 5)

school_system.display_student_info(student_ivanenko)
