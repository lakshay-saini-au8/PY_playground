class Student:
    def __init__(self, name, id, age, batch_id):
        self.name = name
        self.id = id
        self.age = age
        self.batch_id = batch_id
        self.subjects = []


class Subject:
    def __init__(self):
        self.id = None
        self.name = None

    def create_student(self, name, id, age, batch_id):
        self.newStudent = Student(name, id, age, batch_id)

    def add_subject(self, id, name):
        self.id = id
        self.name = name
        self.newStudent.subjects.append([self.id, self.name])

    def remove_subject(self, id):
        subjectData = self.newStudent.subjects
        for index, value in enumerate(subjectData):
            if value[0] == id:
                subjectData.remove(value)

    def show_all_subjects(self):
        print(self.newStudent.subjects)


s1 = Subject()
s1.create_student("Lakshay", "2", "20", "2013")
s1.add_subject("20", "Social")
s1.add_subject("21", "English")
s1.show_all_subjects()
s1.remove_subject("21")
s1.add_subject("22", "Maths")
s1.show_all_subjects()
