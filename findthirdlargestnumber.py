numbers = [10, 45, 23, 67, 45, 89, 12]

largest = 0
second = 0
third = 0

for num in numbers:

    if num > largest:
        third = second
        second = largest
        largest = num

    elif num > second:
        third = second
        second = num

    elif num > third:
        third = num

print(third)