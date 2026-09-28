nums = 583246
count = 0

while nums > 0:
    digit = nums % 10
    nums = nums // 10
    if digit % 2 == 1:
        count+=1
print(count)