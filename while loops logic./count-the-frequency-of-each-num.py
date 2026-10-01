numbers = [2, 3, 2, 5, 3, 2, 4]
i = 0
freq = {}

while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] =freq[numbers[i]] + 1
    else:
         freq[numbers[i]] = 1
    i += 1
print(freq)     
