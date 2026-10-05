numbers = [4,2,7,2,9,4,5,7,8,]
i=0
freq={}

while i < len(numbers):
    if numbers[i] in freq:
        freq[numbers[i]] = freq[numbers[i]] + 1
    else:
        freq[numbers[i]] = 1
    i +=1 

print(freq)   
