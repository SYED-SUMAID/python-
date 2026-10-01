numbers = [4, 7, 2, 9, 7, 3, 2]
i = 0
seen = []

while i < len(numbers):
    if numbers[i] in seen:
        print(numbers[i])
        break
    else:
        seen.append(numbers[i])
    i +=1
    