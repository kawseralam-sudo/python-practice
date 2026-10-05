class Student:
    def __init__(self,name,roll,dep):
        self.name = name
        self.roll = roll
        self.dep = dep

    def show_detials(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("dep:",self.dep)

student1 = Student("Kawsar", 22, "CSE")
student2 = Student("Rahim", 21, "EEE")
print("==========student1=======")
student1.show_detials()

print()

print("==========student2=======")
student2.show_detials()