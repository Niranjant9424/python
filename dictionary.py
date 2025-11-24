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

# get() we use get in order to get a value when you mention key we can do it calling key but when there is no key it gives an error but by get method we wont get an error instead a none value
print(stu_data4.get('subject'))
