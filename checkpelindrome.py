word = "racecar"

def pelindrome(word):

   if word == word[::-1]:
    return True
   else:
    return False

print(pelindrome(word))   