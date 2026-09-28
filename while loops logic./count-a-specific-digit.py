num = 987654321
count = 0

while num > 0:
    digit = num % 10
    num = num // 10
    if digit == 5:
        count +=1
print(f"digit 5 appears {count} times")