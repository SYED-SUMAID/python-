numbers = [23,45,67,34,76,54,32,23,34,56,76]

duplicates = []
seen = []
i = 0

while i < len(numbers):

    if numbers[i] in seen:

        if numbers[i] not in duplicates:
            duplicates.append(numbers[i])

    else:
        seen.append(numbers[i])

    i += 1

print(duplicates)