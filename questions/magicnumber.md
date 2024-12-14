## Magic Number

**Description:**
A number is considered magical if the sum of its digits is divisible by 7. Your task is to create a function `is_magic_number(number)` that checks whether a number is magical.

The function takes a positive integer (number) as input and returns:

-   `True` if the sum of its digits is divisible by 7.
-   `False` otherwise.

**Examples:**

```python
# Example 1
print(is_magic_number(28))  # Output: False (2 + 8 = 10, and 10 % 7 != 0)

# Example 2
print(is_magic_number(123))  # Output: False (1 + 2 + 3 = 6, and 6 % 7 != 0)

# Example 3
print(is_magic_number(7007))  # Output: True (7 + 0 + 0 + 7 = 14, and 14 % 7 == 0)
```

**Rules:**

1. Input must be a positive integer.
2. There is no limit on the number of digits (e.g., 7007, 123456789, etc.).
3. The sum of digits must be calculated correctly, regardless of the number of digits.

**Note:**
You can use string manipulation or mathematical operations to calculate the sum of digits.

Have fun finding the magic numbers! ✨