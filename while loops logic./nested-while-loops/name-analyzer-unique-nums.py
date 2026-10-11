numbers = [4,2,7,2,9,4,5,7,8]

i = 0
freq = {}

while i < len(numbers):

    if numbers[i] in freq:
        freq[numbers[i]] +=1
    else:
        freq[numbers[i]] = 1

    i +=1   

keys = list(freq) # [4,2,7,9,5,8,]
j = 0
unique_nums = []

while j < len(keys): 
    
    if freq[keys[j]] == 1:
        unique_nums.append(keys[j])

    j += 1

print(unique_nums)