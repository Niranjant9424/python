# module:- a single python file

# create a module named mymodule.py

# Use that module here using import
from math import factorial  # same library example
import math  # library example
from mymodule import p1  # trying to import a specific variable
import mymodule
mymodule.greetings('niranjan')

# use specific part of code or variable from myimport
print(p1['name'])

# packages :- collection of modules /py files + __init__.py file is package

# libraries:- collection of modules and packages are libraries ex:- pandas,math.matplotlib
a = 16
print(math.sqrt(a))

print(factorial(4))
