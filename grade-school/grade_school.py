class School(object):
        def __init__(self):
            self.list_of_students = []

        def add_student(self, name, grade):
            student_to_add = Student(name, grade)
            self.list_of_students.append(student_to_add)

        def roster(self):
            names_list = []
            for student in self.list_of_students:
                names_list.append(student.name)
            return sorted(names_list)

        def grade(self, grade_number):
            grade_list = []
            for grades in self.list_of_students:
                if grades.grade == grade_number:
                    grade_list.append(grades.name)
            return sorted(grade_list)





class Student(object):
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade






