# 🔹 Python Problem-Solving Challenges

## Problem 1: Reverse a String
### Description:
Write a function that takes a string as input and returns the reversed string.

### Example:
**Input:** `"hello"`  
**Output:** `"olleh"`

### Solution:
```python
message = "hello"
print(message[::-1])    
```

### Output:
```
olleh
```

---

## Problem 2: Count Vowels in a String
### Description:
Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).

### Example:
**Input:** `"Apple"`  
**Output:** `2`

### Solution:
```python
def count_vowels(s):
    count = 0
    for char in s.lower():  # Convert to lowercase and loop through each character
        if char in "aeiou":  # Check if it's a vowel
            count += 1
    return count

print(count_vowels("Pineapple"))
```

### Output:
```
4
```

---

## Problem 3: Sum of Digits
### Description:
Write a function that takes a non-negative integer and returns the sum of its digits.

### Example:
**Input:** `1234`  
**Output:** `10`

### Solution:
```python
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))
```

### Output:
```
10
```

