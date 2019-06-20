def Inp():
    a=int(input("first number: "))
    b=int(input("second number: "))
    return a,b
def add():
    a,b=Inp()
    Sum = a+b
    return Sum
def op():
    Sum=add()
    print("sum: ",Sum)
