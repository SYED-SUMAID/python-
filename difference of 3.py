numbers = [1,4,7,10,12]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[j] - numbers[i] == 3:
         print(numbers[i],numbers[j])