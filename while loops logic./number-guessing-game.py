secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number: "))

print("Congratulations! You guessed it.")