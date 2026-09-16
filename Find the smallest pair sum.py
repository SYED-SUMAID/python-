numbers = [8,3,7,2,9,4]

smallest = numbers[0] + numbers[1]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        pair_sum = numbers[i] + numbers[j]

        if pair_sum < smallest:
            smallest = pair_sum
print(smallest)
