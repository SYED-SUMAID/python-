num = 58327
smallest = 9

while num > 0:
    digit = num % 10
    num = num // 10
    if digit < smallest:
        smallest = digit
print(smallest)