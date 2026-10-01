numbers = [4, 7, 2, 9, 7, 3, 2, 5, 4]
i = 0
seen = []

while i < len(numbers):
    if numbers[i] in seen:
        print(numbers[i])
    else:
        seen.append(numbers[i])
    i +=1
