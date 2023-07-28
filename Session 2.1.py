import math
op= input("Enter operation(+,-,*,/,sin,cos,tan,cot,!)= ")


if op == "+":
    a= float(input("Enter a= "))
    b= float(input("Enter b= "))
    print(float(a + b))
if op == "-":
    a= float(input("Enter a= "))
    b= float(input("Enter b= "))
    print(float(a - b))
if op == "*":
    a= float(input("Enter a= "))
    b= float(input("Enter b= "))
    print(float(a * b))
if op == "/":
    a= float(input("Enter a= "))
    b= float(input("Enter b= "))
    print(float(a / b))
    if b == 0:
        print("Invalid")
if op == "sin":
    x= float(input("Enter x= "))
    print(math.sin(x))
if op == "cos":
    x= float(input("Enter x= "))
    print(math.cos(x))
if op == "tan":
    x= float(input("Enter x= "))
    print(math.tan(x))
if op == "cot":
    x= float(input("Enter x= "))
    print(math.cos(x) / math.sin(x))
if op == "!":
    x= int(input("Enter x= "))
    print(math.factorial(x))
