numbers = [2, 3, 7, 8, 5, 5]

count = 0

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == 10:
               count +=1
print(count)
