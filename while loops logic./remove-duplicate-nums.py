numbers = [4,2,7,2,9,4,5,7,8]
i = 0
seen = []

while i < len(numbers):
    if numbers[i] not in seen:
        seen.append(numbers[i])
    i +=1    

print(seen)    