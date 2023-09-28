 # Define a Student class
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the student list based on CGPA in descending order
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Test the function with a list of student objects
students = [
    Student("Kholi", "R001", 3.4),
    Student("Rohit", "M002", 3.7),
    Student("Dhoni", "C003", 4.0),
    Student("Pandya", "G004", 3.5)
]

sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))