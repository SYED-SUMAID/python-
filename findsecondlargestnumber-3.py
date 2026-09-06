numbers = [10, 45, 23, 67, 45, 89, 12]

largest = max(numbers)

second_largest = numbers[0]

for num in numbers:
    if num != largest and num > second_largest:
        second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)