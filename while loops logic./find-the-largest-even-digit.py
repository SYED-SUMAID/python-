num = 58392746
largest = 0

while num > 0:
    digit = num % 10 
    num = num // 10
    if digit % 2 == 0 and digit > largest:
        largest = digit
print(largest)