# # file handling

# # Open a file
# file = open('filehandling\data.txt', 'r')

# # read the file :- read method
# file = open('filehandling\data.txt', 'r')
# contents = file.read()  # reads entire content
# print(contents)
# file.close()

# # 2. readline method
# file = open('filehandling\data.txt', 'r')
# contents = file.readline()  # reads only first line
# print(contents)
# file.close()

# # 3. readlines method
# file = open('filehandling\data.txt', 'r')
# contents = file.readlines()  # reads line as list
# print(contents)
# file.close()


# # WRITE MODE
# # opens a file if file is not present
# file = open('filehandling\example2.txt', 'w')
# # if you add another data that will overwrite the file for that not to happen we use append
# file.write("hello niranjan how are you :) ")
# file.close()

# # APPEND MODE
# file = open('filehandling\example2.txt', 'a')
# file.write("\ngood to see you amigo")
# file.close()


# # close a file
# # 2 methods 1. using with statement 2. using exception handling
# with open('filehandling\example2.txt', 'r') as file:
#     content = file.read()
#     print(content)
