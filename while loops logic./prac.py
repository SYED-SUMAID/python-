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

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")    
print("5. Modulus")
print("6. Exponent")

choice = input("Enter choice(1/2/3/4/5/6): ")

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))    

if choice == '1':
    print("Addition:", add(input1, input2))
elif choice == '2':
    print("Subtraction:", subtract(input1, input2))
elif choice == '3':                            
    print("Multiplication:", multiply(input1, input2))
elif choice == '4':
    print("Division:", divide(input1, input2))  

