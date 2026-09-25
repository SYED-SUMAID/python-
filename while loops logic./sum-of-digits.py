num = 786
total = 0

while num > 0:
    digit = num % 10 
    # 6 ,7,8
    num = num // 10  # 78,7
    total =total + digit

print(total)