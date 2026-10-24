def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulus(a,b):
    return a % b


def exponent(a, b):
    return a ** b

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))    

if input == 1:
    print("Addition:", add(input1, input2))
elif input == 2:
    print("Subtraction:", subtract(input1, input2))
elif input == 3:                            
    print("Multiplication:", multiply(input1, input2))
elif input == 4:
    print("Division:", divide(input1, input2))  
