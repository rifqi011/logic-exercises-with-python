## Treasure Hunt Challenge

**Story:**
On a mysterious island, there's a treasure chest locked with a secret code. To unlock it, you need to solve a riddle. As a treasure hunter, you've found a scroll with the following clue:

> "Take all the numbers in a list. Multiply only the even numbers together. If there are no even numbers, just say 1."

**Your Mission:**
Write a Python function called `treasure_code(numbers)` that:

-   Takes a list of numbers as input.
-   Multiplies all the even numbers in the list.
-   If there are no even numbers, returns 1.

**Example:**

```python
# Example 1
numbers = [2, 3, 4, 5]
print(treasure_code(numbers))  # Output: 8 (because 2 * 4 = 8)

# Example 2
numbers = [1, 3, 5]
print(treasure_code(numbers))  # Output: 1 (no even numbers)

# Example 3
numbers = [6]
print(treasure_code(numbers))  # Output: 6 (only one even number)
```

**Rules:**

1. Don't use built-in functions like `prod` from the `math` library.
2. Your code should work with empty lists, negative numbers, and mixed number types.

**Ready to find the treasure?** Let's use code to crack the secret!
