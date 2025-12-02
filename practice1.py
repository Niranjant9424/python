class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def student_details(self):
        print(
            # same method name
            f"the name of the student is {self.name} and age is {self.age} and gender is {self.gender}")


# child class
class grad_Student(Student):
    def __init__(self, name, age, gender, percentage):
        super().__init__(name, age, gender)   # values inherit from parent class
        self.percentage = percentage

    def student_details(self):
        print(
            # same method name
            f"the name of the student is {self.name} and age is {self.age} and gender is {self.gender} and percentage is {self.percentage}")


# object
grad1 = grad_Student('niranjan', '21', 'male', 99)
student1 = Student('niranjan', 21, "male")
grad1.student_details()
# botH ARE of same method name but performs differently based on the class they belong to
student1.student_details()
