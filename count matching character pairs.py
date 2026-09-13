word = "aabbc"

count = 0

for i in range(len(word)):
    for j in range(i+1,len(word)):
        if word[i] == word[j]:
           count +=1
print(count)            