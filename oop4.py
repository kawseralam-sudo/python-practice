class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):

    def __init__(self, name, age,dep):
        super().__init__(name, age)
        self.dep=dep
        
    def show_details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("dep:",self.dep)


student1 = Student("Kawsar", 22, "CSE")
student2 = Student("Rahim", 21, "EEE")

print("========== Student 1 ==========")
student1.show_details()

print()

print("========== Student 2 ==========")
student2.show_details()