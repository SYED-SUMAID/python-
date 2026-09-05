#numbers = [4, 9, 2, 7, 1]


def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num >  largest:
         largest = num

    return largest

numbers = input("Enter the numbers:")
numbers = numbers.split(",")

max_numbers = []

for num in numbers:
   max_numbers.append(int(num))

   numbers = max_numbers

print(largest_number(numbers))   


   