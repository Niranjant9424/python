# # Tuple packing and unpacking
# a = "niranjan"
# b = 21
# c = "doctor"
# tuple_pack = a, b, c
# print(tuple_pack)
# name, age, profession = tuple_pack
# print(name)
# print(age)
# print(profession)

# # trying to modify elements in a tuple
# a = (1, 2, 3, 4, 5)
# list_elements = list(a)
# print(list_elements)
# list_elements.append(6)
# print(list_elements)
# tuple1 = tuple(list_elements)
# print(tuple1)

# tuple functions
a = (1, 2, 3, 4)
# print(len(a))

sorted_data = tuple(sorted(a))
print(sorted_data)

print(sum(a))

print(min(a))

print(max(a))
