def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test with different input lists of students
students_list = [
    Student("Devi", "2021001", 3.9),
    Student("Gowtham", "2021002", 3.7),
    Student("Devasri", "2021003", 3.8),
    Student("divya", "2021004", 3.6)
]

sorted_students = sort_students(students_list)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

