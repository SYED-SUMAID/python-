numbers = [7, 3, 5, 2, 8, 4]

smallest = numbers[0] * numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        smallest_product = numbers[i] * numbers[j]

        if smallest_product < smallest:
            smallest = smallest_product

print(smallest)