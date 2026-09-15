numbers = [2, 3, 4, 5, 6, 8]

for i  in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]*numbers[j] == 24:
            print(numbers[i],numbers[j])