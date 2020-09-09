class Student:
    def __init__(self, name, id, age, batch_id):
        self.name = name
        self.id = id
        self.age = age
        self.batch_id = batch_id
        self.subjects = []

    def show_details(self):
        print("Student Details:")
        print()
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")
        print(f"Age:{self.age}")
        print(f"Batch ID: {self.batch_id}")
        print()
        print("Subject List:")
        print()
        [print(f"{subId}:{subName}") for subId, subName in self.subjects]


class Subject:
    def __init__(self, newStudent):
        self.id = None
        self.name = None
        self.newStudent = newStudent

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
        print("Subject List:")
        print()
        [print(f"{subId}:{subName}")
         for subId, subName in self.newStudent.subjects]


student1 = Student("Lakshay", "2", "22", "Ramanujan")
s1 = Subject(student1)
s1.add_subject("CS102", "Data Structure")
s1.add_subject("CS104", "Operating System")
s1.remove_subject("CS104")
s1.add_subject("CS105", "Computer Networks")
# s1.show_all_subjects()
student1.show_details()
