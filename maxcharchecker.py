text = "banana"

def max_char_count(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

    max_char = ""
    max_count = 0

    for char in frequency:
        if frequency[char] > max_count:
            max_count = frequency[char]
            max_char = char

    return max_char , max_count

print(max_char_count(text))        

