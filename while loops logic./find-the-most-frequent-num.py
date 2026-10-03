numbers = [4,2,7,2,9,2,4,7,4,4,4]
i = 0
freq = {}
while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] = freq[numbers[i]] + 1
    else:
        freq[numbers[i]] = 1

    i +=1
print(freq)   

keys = list(freq)#[4,2,7,9]

j = 0
max_count = 0
m0st_freq = 0

while j < len(keys):
    if freq[keys[j]] > max_count:
        max_count = freq[keys[j]]
        m0st_freq = keys[j]
    j+=1
                
print(m0st_freq)