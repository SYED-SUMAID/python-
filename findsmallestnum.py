numbers = [4,56,7,8,1]

def smallest_num(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest        

print(smallest_num(numbers))