num = 121
num2 = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse *10 + digit
    num = num //10
    if reverse == num2:
     
     print("yes this is a pelindrome")