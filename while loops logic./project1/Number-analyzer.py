numbers = [4,2,7,2,9,4,5,7,8,]
i=0
highest_num = numbers[0]

while i < len(numbers):
    if numbers[i] > highest_num:
        highest_num = numbers[i]
    i+=1
print(highest_num)

j = 0
smallest_num = numbers[0]

while j < len(numbers):
    if numbers[j] < smallest_num:
        smallest_num = numbers[j]
    j+=1
print(smallest_num)

k = 0  
total = 0

while k < len(numbers):
    total = total + numbers[k]
    k+=1

print(total) 

even_nums = []
odd_nums = []

l = 0

while l < len(numbers):
    if numbers[l] % 2 == 0:
        even_nums.append(numbers[l])
    else:
        odd_nums.append(numbers[l])
    l +=1   

print(even_nums)
print(odd_nums)

m = 0
seen = []

while m < len(numbers):
    if numbers[m] not in seen:
        seen.append(numbers[m])
    m +=1    
print(seen)