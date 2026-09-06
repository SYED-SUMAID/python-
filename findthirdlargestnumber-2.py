numbers = [10, 45, 23, 67, 45, 89, 12]

largest = max(numbers)
numbers.remove(largest)

second_largest = max(numbers)
numbers.remove(second_largest)

third_largest = max(numbers)

print("Third largest:", third_largest)