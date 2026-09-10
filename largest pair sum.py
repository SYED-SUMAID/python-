# Find the largest pair of sum
numbers = [4,7,2,9,5]
largest = 0

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        pair_sum = numbers[i] + numbers[j]
        if pair_sum > largest:
         largest = pair_sum
print(largest)