class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self,name,age):
        print("Name:", self.name)
        print("Age:", self.age)
Student1 = Student("Alice", 20)
Student1.display("hero",17)