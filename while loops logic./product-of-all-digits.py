num=583
product=1

while num >0:
    digit = num % 10
    num = num // 10
    product = product * digit
print(product)