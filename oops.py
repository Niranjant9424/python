# two ways of programming in python
# 1. procedural programming
# 2.OOPs
# oops:- basically in oops we are trying to organize code by creating classes(ex:- blueprint of a house)
# which are also known as blueprint with that we can create real world objects(ex :- house)

# class:- its a blueprint or template for creating objects
# classes defines 2 main things
# 1. attributes(data):- it defines properties (variables inside a class they store data or state of a object)
# two types of attributes
#  1.instance attributes(unique like brand color car()):- defined inside _init_
#  2. class attributes(common 4wheels common in car ):- defined inside class but outside methods
# 2. methods(actions):- actions and behaviour (functions inside a class where they perform actions or behaviour)
# objects:- an object is a specific instance of a class
# it has actual data based on blueprint defined by class


# oops:- syntax

# class :- its just a blueprint like for example
# you are creating a car blueprint with that blueprint you can create any no of cars(objects)
# class Student:
#     pass


# object:- instance of a class
# student1 = Student()

# what is self
# self means this object when you are in a class self means using that object which you have called

# 6. Constructor (__init__)

# A constructor is a special method that runs automatically when you create an object.

# Example:

# def __init__(self, brand, color):
#     self.brand = brand       # attribute
#     self.color = color       # attribute


# This sets the object’s initial values.


# CREATING A CLASS
# class Student:
#     def __init__(self, name, age, gender, team):  # constructor method
#         self.name = name     # instance attributes :- Values are unique to each and every object
#         self.age = age
#         self.gender = gender
#         self.team = team

#     # another method #example for abstraction as it is hidden from users
#     def student_details(self):
#         print(
#             f"student name is {self.name} and age is {self.age} and gender is {self.gender}")


# # creating a variable inside class and linking it to object
# team1 = 'a'
# team2 = 'b'


# # CREATING AN OBJECT
# s1 = Student("niranjan", 21, "male", team1)
# s2 = Student("arjun", 21, "male", team2)

# # IF YOU NEED S1 OBJECT DATA IN DICTIONARY FORM
# print(s1.__dict__)

# # GENERAL OBJECT DATA
# s1.student_details()
# s2.student_details()

# # MODIFY OBJECT PROPERTY OR ATTRIBUTES
# # in s1 object i want to change age to 22
# s1.age = 22
# print(s1.__dict__)


# # DELETING A OBJECT PROPERTY OR ATTRIBUTE LIKE GENDER
# del s1.gender
# print(s1.__dict__)

# # delete an object
# del s1


# features of OOPs
# 1. abstraction
# 2.encapsulation
# 3.polymorphism
# 4.inheritance

# 1. abstraction:- hiding complex details and showing only neccesary parts
# 2. encapsulation:- wrapping data(properties) and methods(functions) in a single unit(class) and controlling how the data can be accesed outside the class
# example
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.__color = color  # private property
# private property getter method(get the value)

    def get_color(self):
        return self.__color
# private property setter method(set the value)

    def set_color(self, color):
        self.__color = color


c1 = Car("hyundai", "blue")
print(c1.get_color())
c1.set_color('black')
print(c1.get_color())


# 3. inheritance :- allows one class(child) to inherit properties and methods from another class (parent) is inheritance
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def student_details(self):
        print(
            f"the name of the student is {self.name} and age is {self.age} and gender is {self.gender}")


# child class
class grad_Student(Student):
    def __init__(self, name, age, gender, percentage):
        super().__init__(name, age, gender)   # values inherit from parent class
        self.percentage = percentage

    def student_details(self):
        super().student_details()  # methods inherit from parent class
        print(f"and percentage is {self.percentage}")


# object
grad1 = grad_Student('niranjan', '21', 'male', 99)
print(grad1.__dict__)
grad1.student_details()


# 4. polymorphism :- same method name but performs as per they class

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
