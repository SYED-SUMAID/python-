numbers = [1, 2, 3, 4, 5, 6]

count = 0

for i in range(len(numbers)):
    for j in range(i+1,(len(numbers))):
        odd_sum = numbers[i] + numbers[j]

        if odd_sum % 2 == 1:
         count+=1

print(count)
