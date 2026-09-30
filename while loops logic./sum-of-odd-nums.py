num = 583246
total = 0

for i in str(num):
    if int(i) % 2 == 1:
        total += int(i)
print(total)