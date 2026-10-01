numbers = [45, 12, 89, 7, 34, 67]

i = 0
smallest = numbers[0]
second_smallest = numbers[1]

while i < len(numbers):

    if numbers[i] < smallest:
        second_smallest = smallest
        smallest = numbers[i]

    elif numbers[i] < second_smallest and numbers[i] != smallest:
        second_smallest = numbers[i]

    i += 1

print(second_smallest)