def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    x = input("Calculator: Addition | Subtraction | Multiplication | Division | Exit").lower()
    if x == "addition":
        print(f"Ans: {add(num1, num2)}")
    elif x == "subtraction":
        print(f"Ans: {subtract(num1, num2)}")
    elif x == "multiplication":
        print(f"Ans: {multiply(num1, num2)}")
    elif x == "division":
        print(f"Ans: {divide(num1, num2)}")
    elif x == "exit":
        print("Cya!")
        break
    else:
        print("Command doesn't exist!")