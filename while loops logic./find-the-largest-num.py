num = 58327
largest = 0

while num > 0:
    digit = num % 10
    num = num //10
    if digit > largest:
        largest = digit
print(largest)