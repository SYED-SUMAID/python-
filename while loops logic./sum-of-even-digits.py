num = 583246
total = 0

while num > 0:
    digit = num % 10
    num = num // 10
    if digit % 2 == 0:
        total +=digit
print(total)
