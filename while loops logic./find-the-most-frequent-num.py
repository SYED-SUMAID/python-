numbers = [4,2,7,2,9,2,4,7]
i = 0
freq = {}

while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] = freq[numbers[i]] + 1
    else:
        freq[numbers[i]] = 1

    i += 1

keys = list(freq)

j = 0
max_count = 0
most_frequent = 0

while j < len(keys):
    if freq[keys[j]] > max_count:
        max_count = freq[keys[j]]
        most_frequent = keys[j]

    j +=1

print(most_frequent)