from datetime import datetime
from func import SchoolSystem

school_system = SchoolSystem()

school_system.add_student(1, "Student 1", datetime.now())
school_system.add_student(2, "Student 2", datetime.now())

school_system.add_teacher(1, "Teacher 1", datetime.now())
school_system.add_teacher(2, "Teacher 2", datetime.now())

school_system.add_subject(1, "Math")
school_system.add_subject(2, "History")

school_system.add_class(1, "Class A", "10:00 AM", 1, 1)
school_system.add_class(2, "Class B", "1:00 PM", 2, 2)

school_system.enroll_student_in_class(1, 1)
school_system.enroll_student_in_class(2, 2)

school_system.add_grade(1, 1, "A")
school_system.add_grade(2, 2, "B")

school_system.display_student_info(1)
school_system.display_student_info(2)
