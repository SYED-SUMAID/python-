word = "abc"

for i in range(len(word)):
    for j in range(i+1,len(word)):
        print(word[i],word[j])