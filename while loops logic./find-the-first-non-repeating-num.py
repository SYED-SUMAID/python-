numbers = [4,2,7,2,9,4,5,7,8,]
freq = {}
i=0

while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] = freq[numbers[i]] + 1
    else:
        freq[numbers[i]] = 1
    i +=1 
print(freq)    

j = 0

while j < len(numbers):
    if freq[numbers[j]] == 1:
        print(numbers[j])
        break
    j+=1
