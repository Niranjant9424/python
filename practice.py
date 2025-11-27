# 1. find intersection common elements of two lists
list1 = [1, 2, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
set3 = set1 & set2
list3 = list(set3)
print(list3)

# using functions and list comprehension


def intersection_loop(list1, list2):
    return [lst for lst in list1 if lst in list2]


print(intersection_loop(list1, list2))


# Q2 find the most frequent element in a list
numbers = [1, 2, 2, 3, 3, 3, 4]


def most_freq(lst):
    max_count = 0
    most_freq = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            most_freq = item
    return most_freq


print(most_freq(numbers))


# Q3 find cumulative sum of a list
numbers1 = [1, 2, 3, 4]


def cumulative_sum(lst):
    cum_sum = []
    sum = 0
    for item in lst:
        sum += item
        cum_sum.append(sum)
    return cum_sum


print(cumulative_sum(numbers1))


# Q4 remove duplicates from a list
# my answer
fruits = ["apple", "banana", "cherry", "apple", "banana"]
set1 = set(fruits)
list1 = list(set1)
print(list1)

# Q5 find the index of an element of a tuple
my_tuple = (1, 2, 3, 4)


def ele_index(my_tuple):
    value = int(input("enter the no from the tuple you want index of: "))
    for val in range(0, len(my_tuple)):
        if my_tuple[val] == value:
            return val


print(ele_index(my_tuple))

# using tuple index method


def find_index(my_tuple, val):
    return my_tuple.index(val) if val in my_tuple else 'number not in the tuple'


print(find_index(my_tuple, 4))
