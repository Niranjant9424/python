# creating sets
set1 = {1, 2, 3, 4, 5}
print(set1)
# another method to create a set constructor
set2 = set([1, 2, 3, 4, 5])
print(set2)

# set operations
# adding a element
set3 = {1, 2, 3, 4, 5}
set3.add(6)
print(set3)
# removing a element
set3.remove(6)  # it will raise an error if no element is found
print(set3)
set3.discard(5)  # it wont raise an error if no element is found
print(set3)

# set methods
# union method (combines both the elements and remove duplicates)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1.union(set2)  # set1|set2
print(set3)

# intersection (returns the common elements between two)
set4 = {1, 2, 3, 4, 5}
set5 = {3, 4, 5, 6, 7}
set6 = set4.intersection(set5)  # set4 & set5
print(set6)

# difference (returns the difference from the first set)
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6}
c = a.difference(b)   # c=a-b
print(c)

# symmetric difference(element in either set but not in both)
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
set_3 = set_1.symmetric_difference(set_2)  # set_3=set_1^ set_2
print(set_3)  # basically it returns non similar elements from both the sets

# set iteration
# for loop
setA = {1, 2, 3, 4, 5}
for set in setA:
    print(set)
