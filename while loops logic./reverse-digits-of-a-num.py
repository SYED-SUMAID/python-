nums = 12345
reverse=0

while nums > 0:
    digit = nums % 10
    reverse= reverse * 10 + digit
    nums = nums // 10

print(reverse)    