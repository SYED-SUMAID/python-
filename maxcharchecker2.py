text = "banana"

def max_occur_char(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char,0) +1

    max_char = max(freq, key=freq.get)

    return max_char,freq[max_char]


print(max_occur_char(text))
