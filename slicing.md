````markdown
# Python Indexing & Slicing

## Indexing

Used to access a single character.

```python
word = "python"
```

```text
 p  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
word[0]    # p
word[2]    # t
word[-1]   # n
word[-2]   # o
```

Positive index → left to right  
Negative index → right to left

---

## Slicing

Used to get a part of a string/list.

```python
word[start:stop:step]
```

- start → where to start
- stop → where to stop
- step → how much to move

Stop is not included.

```python
word = "python"

word[1:4]      # yth
word[:4]       # pyth
word[2:]       # thon
word[:]        # python
```

---

## Step

```python
word[::2]
```

Takes every 2nd character.

```python
word[::-1]
```

Reverses the string.

Positive step → moves forward  
Negative step → moves backward

---

## Negative Step Example

```python
word = "computer"

word[7:0:-3]
```

Indexes:

```text
7 → 4 → 1
```

Characters:

```text
r → u → o
```

Output:

```text
ruo
```

---

## `-2` Can Mean Different Things

As an index:

```python
word[-2]
```

Means the second character from the end.

As a step:

```python
word[8:2:-2]
```

Means move backwards by 2 indexes.

---

## Palindrome

```python
word == word[::-1]
```

Example:

```python
word = "racecar"

if word == word[::-1]:
    print("Palindrome")
```

---

## How to Solve Slicing

For:

```python
word[8:2:-2]
```

First identify:

```text
start = 8
stop = 2
step = -2
```

Then move:

```text
8 → 6 → 4
```

Stop at `2` because stop is excluded.

Then find the characters at those indexes.

**Remember:**

```text
Indexes → Movement → Characters
```

---

## Quick Revision

```python
word[2]          # index
word[-1]         # last character
word[1:4]        # slicing
word[:4]         # beginning to index 4
word[2:]         # index 2 to end
word[::2]        # every 2nd character
word[::-1]       # reverse
```
````
