def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if b == 0:
        print("cannot divide by ZERO")

    return a/b


def avg(a, b):
    return (a+b)/2


print("select the no which operation you want to perform \
    1. add \
    2.subtract \
    3. multiply \
    4.divide \
    5.avg ")

select = int(input("select a number: "))
a = int(input("enter the first no: "))
b = int(input("enter the second no: "))
if select == 1:
    print(f"the addition of two no's is: {add(a, b)}")

elif select == 2:
    print(f"the subtraction of two no's is: {sub(a, b)}")

elif select == 3:
    print(f"the multiplication of two no's is: {mul(a, b)}")

elif select == 4:
    print(f"the division of two no's is: {div(a, b)}")

elif select == 5:
    print(f"the avg of two no's is: {avg(a, b)}")
