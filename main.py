class Person:
  age = 11
  name = "Oleg"
  def __init__(self, name):
      self.name = name

class Student(Person):
  grade = 0
  def study(self):
    self.grade += 2
  def __init__(self):
      super().__init__("Student")


student = Student()

print(student.grade)
student.study()
print(student.grade)
print(student.grade)
student.study()
print(student.grade)
print(student.grade)
student.study()
print(student.grade)
print(student.grade)
student.study()
print(student.grade)
print(student.grade)
student.study()
print(student.grade)
print(student.grade)
student.study()
print(student.grade)

class Teacher(Person):
  salary = 0
  student = []

  def __init__(self):
      super().__init__("Teacher")
  def teach(self):
    self.salary +=2000 * len(self.students)
  def set_grade(self, students):
    self.students
teacher = Teacher()

print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
print(teacher.salary)
teacher.work
