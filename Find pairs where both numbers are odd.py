numbers = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] % 2 == 1 and numbers[j] % 2 == 1:
            print(numbers[i], numbers[j])