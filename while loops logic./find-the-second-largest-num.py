numbers = 583922741
reverse = 0

while numbers > 0:
    digit = numbers % 10
    numbers = numbers // 10
    reverse = reverse * 10 + digit

seen = []

while reverse > 0:
    digit = reverse % 10
    reverse = reverse // 10 

    if digit in seen:
        print(digit)
        break
    else:
        seen.append(digit)

