````markdown
# Python Loops & Dictionary Logic

## 1. For Loop

A `for` loop processes items one by one.

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

Output:
```text
10
20
30
```

---

## 2. Loop Through a String

```python
word = "python"

for char in word:
    print(char)
```

Each iteration gives one character.

---

## 3. Loop Through a Dictionary

```python
data = {
    "name": "Sumaid",
    "age": 21
}
```

### Keys

```python
for key in data:
    print(key)
```

A normal dictionary loop gives **keys**.

### Values

```python
for value in data.values():
    print(value)
```

### Keys + Values

```python
for key, value in data.items():
    print(key, value)
```

Remember:

```text
data          → keys
data.values() → values
data.items()  → key + value
```

---

## 4. `if` Inside a Loop

Used to filter or check items.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num > 3:
        print(num)
```

Output:
```text
4
5
```

---

## 5. Counter

Use a counter when you need to count something.

```python
count = 0

for num in numbers:
    if num > 3:
        count += 1
```

`count += 1` means:

```python
count = count + 1
```

---

## 6. Accumulator

Use an accumulator when you need to build a value.

```python
total = 0

for num in numbers:
    total += num
```

---

## 7. Frequency Dictionary

Useful for counting occurrences.

```python
word = "banana"
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
```

Result:

```python
{'b': 1, 'a': 3, 'n': 2}
```

Logic:

```text
Exists → increase
New    → set to 1
```

---

## 8. `break`

Stops the loop.

```python
for num in numbers:
    if num == 3:
        break
```

---

## 9. `continue`

Skips the current iteration.

```python
for num in numbers:
    if num == 3:
        continue
    print(num)
```

---

## 10. `range()`

Used to generate a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

`range(5)` → `0` to `4`

---

## 11. Loop Logic

When solving a loop problem, identify:

```text
What am I looping over?
What does one iteration give me?
What condition do I need?
What result am I building?
```

Common patterns:

```text
Loop + if       → filtering
Loop + counter  → counting
Loop + total    → sum/accumulation
Loop + dict     → storing/counting
Loop + break    → stop when found
```

### Key Idea

Understand what happens to **one item** first.

Then let the loop repeat that logic.
````
