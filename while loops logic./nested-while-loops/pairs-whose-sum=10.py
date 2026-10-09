numbers = [4,2,7,2,9,4,5,7,8,]
i = 0

target =  10

while i < len(numbers):
    j = i + 1

    while  j < len(numbers):
        if numbers[i] + numbers[j] == target:
         print(numbers[i],numbers[j])
            
        j+=1

    i+=1