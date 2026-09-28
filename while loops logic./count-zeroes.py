num = 10203040
count = 0

while num > 0:
    digit = num % 10
    num = num // 10
    if digit == 0:
        count +=1
print(count)