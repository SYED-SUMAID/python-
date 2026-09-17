numbers = [2,5,3,8,4,6]

largest = numbers[0]*numbers[1]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        largest_product = numbers[i]*numbers[j]

        if largest_product > largest:
            largest = largest_product

print(largest)            