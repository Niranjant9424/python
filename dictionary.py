# dictionary:- data structure in python that stores data in a key value pair
# it is ordered changeable nd do not allow duplicates
# key:- unique immutable (strings,tuple,numbers)
# value: not unique (any data type)

# CREATING A DICTIONARY

# METHOD1
stu_data = {
    'name': 'niranjan',
    'age': 21,
    'gender': 'male'
}
print(stu_data)

# METHOD2 (USING DICT CONSTRUCTOR)
person = dict(name="niranjan", age=21, gender="male")
print(person)

# METHOD 3 (USING A LIST OF TUPLES ( A LIST CONATINING TUPLE VALUES))
person1 = dict([("name", "niranjan"), ("age", 21), ("gender", "male")])
print(person1)

# TO ACCESS DICTIONARY VALUES
stu_data1 = {
    'name': 'niranjan',
    'age': 21,
    'gender': 'male'
}
# dictionary-name[key value]
print(stu_data1['name'])


# DICTIONARY ADD MODIFY OR REMOVE ITEMS
student = {
    'name': 'niranjan',
    'age': 21,
    'gender': 'male'
}

# add items

student['rollno'] = 'G0'
print(student)

# modify/replace items

student['age'] = 22
print(student)

# delete items (either by del(permanantly delete) or pop(you can delete and store the value))
# remove del
del student['rollno']
print(student)
# pop and store the value
age = student.pop("age")
print(age)

# DICTIONARY METHODS
'''
1. keys()
2.values()
3. items()
4.get()
'''

stu_data4 = {
    'name': 'niranjan',
    'age': 21,
    'gender': 'male'
}

# keys()
print(stu_data4.keys())

# values()
print(stu_data4.values())

# items()
print(stu_data4.items())

# get() basically to get a value we use get method it is similar to key but when the specified key is absent it raises an error but by get method it wont raise an error
print(stu_data4.get('subject'))


# DICTIONARY ITERATIONS

stu_data5 = {
    'name': 'niranjan',
    'age': 21,
    'gender': 'male'
}

# using keys and printing only keys
for key in stu_data5:
    print(key)

# using values and printing values
for value in stu_data5:
    print(stu_data5[value])

# using keys() method
for keys in stu_data5.keys():
    print(keys)

# using values() method
for values in stu_data5.values():
    print(values)

# To print both (key,value) pair
for keys, values in stu_data5.items():
    print(keys, ":", values)

# NESTED DICTIONARY
students_data = {
    'student1': {'name': 'niranjan', 'age': 21, 'gender': 'male'},
    'student2': {'name': 'arjun', 'age': 21, 'gender': 'male'}
}

# accessing values
print(students_data['student1'])

# DICTIONARY COMPREHENSION
# Syntax
# new_dict=
# {key expresion: value expression for item in iterable if condition}

my_dict = {x: x*x for x in range(1, 6)}
print(my_dict)
