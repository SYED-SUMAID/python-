numbers = [1, 2, 4, 5, 6, 8, 9]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] % 2 ==0 and numbers[j] % 2 ==0:
          print(numbers[i],numbers[j])