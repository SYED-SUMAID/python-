num = 58392741
total = 0

while num > 0:
    digit = num % 10
    num = num // 10
    if digit > 5:
        total += digit
print(total)        