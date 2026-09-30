num = 58392741
smallest = 9

while num > 0 :
    digit = num % 10
    num = num // 10
    if digit % 2 == 1 and digit < smallest:
        smallest = digit
print(smallest)