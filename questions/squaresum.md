## Square Sum

**Description:**  
Your task is to create a function `square_sum(numbers)` that takes a list of integers (`numbers`), squares each number in the list, and then sums the squared values together.

The function should return the total sum of the squared values.

**Examples:**

```python
# Example 1
print(square_sum([1, 2, 2]))  # Output: 9 (1^2 + 2^2 + 2^2 = 9)

# Example 2
print(square_sum([0, 3, 4, 5]))  # Output: 50 (0^2 + 3^2 + 4^2 + 5^2 = 50)

# Example 3
print(square_sum([-1, -2]))  # Output: 5 ((-1)^2 + (-2)^2 = 5)
```

**Rules:**

1. The input is a list of integers.
2. The list may contain positive, negative, or zero values.
3. The function must handle an empty list and return `0` in that case.

**Note:**  
Use list comprehensions or loops to simplify your implementation. Have fun squaring and summing! ✨
