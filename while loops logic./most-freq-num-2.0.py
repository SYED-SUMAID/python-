numbers = [4, 2, 7, 2, 9, 4, 5, 7, 8]

i = 0
freq = {}

while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] += 1
    else:
        freq[numbers[i]] = 1

    i += 1

    keys = list(freq)
j = 0
max_freq = 0

# First, find the highest frequency
while j < len(keys):
    if freq[keys[j]] > max_freq:
        max_freq = freq[keys[j]]

    j += 1

# Then, collect every number with that frequency
j = 0
most_frequent = []

while j < len(keys):
    if freq[keys[j]] == max_freq:
        most_frequent.append(keys[j])

    j += 1

print("Most frequent numbers:", most_frequent)
print("Highest frequency:", max_freq)