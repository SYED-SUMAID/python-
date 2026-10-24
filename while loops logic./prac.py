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

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))    

if choice == '1':
    print("Addition:", add(number1, number2))
elif choice == '2':
    print("Subtraction:", subtract(number1, number2))
elif choice == '3':                            
    print("Multiplication:", multiply(number1, number2))
elif choice == '4':
    print("Division:", divide(number1, number2))
elif choice == '5':
    print("Modulus:", modulus(number1, number2))
elif choice == '6':
    print("Exponent:", exponent(number1, number2))
