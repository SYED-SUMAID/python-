numbers = [1,2,3,4,6,7,8,9,10]
i = 0
expected_total = 0

while i <= 10:
    expected_total +=i
    i+=1
print(expected_total)
actual_total = 0
j = 0

while j < len(numbers):
    actual_total += numbers[j]
    j+=1
print(actual_total)

missing_number = expected_total - actual_total
print(missing_number)