class School(object):
    def __init__(self):
        self.list_of_students = []
        pass

class Student(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def add_student(self):
        return '{},{}'.format(self.name,self.grade)



student1 = Student("Tanika",3)
student2 = Student("Aayan",4)
print(student2.add_student())



