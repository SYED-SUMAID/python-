numbers = [10,45,23,67,45,89,12]

def second_largest(numbers):
    largest_no = 0
    secondlargest_no = 0

    for num in numbers:
        if num > largest_no:
            second_largest = largest_no
            largest_no = num
        elif num > secondlargest_no:
            secondlargest_no = num
    return second_largest
      


print(second_largest(numbers))