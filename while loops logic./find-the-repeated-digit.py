num = 58392785
reverse = 0

while num > 0:
    digit = num % 10
    num = num // 10
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