numbers = [12, 45, 7, 89, 34, 67]

i = 0
largest = 0
second_largest = 0

while i < len(numbers):
    if numbers[i] > largest:
         second_largest = largest
         largest =  numbers[i]
    elif numbers[i] > second_largest and numbers[i] != largest:
         second_largest = numbers[i]
    i += 1
print(second_largest)    