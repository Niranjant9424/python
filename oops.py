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


# creating a class
class Student:
    def __init__(self, name, age, gender):  # constructor method
        self.name = name     # instance attributes :- Values are unique to each and every object
        self.age = age
        self.gender = gender

    def student_details(self):  # another method
        print(
            f"student name is {self.name} and age is {self.age} and gender is {self.gender}")


# creating an object
s1 = Student("niranjan", 21, "male")
s2 = Student("arjun", 21, "male")

# if you need s1 object data in dictionary form
print(s1.__dict__)

# general object data
s1.student_details()
s2.student_details()
