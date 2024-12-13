## Leap Year Checker Challenge

**Story:**
A scientist is studying an ancient calendar and has discovered that certain years are leap years. Leap years follow specific rules:

-   A year is a leap year if it is divisible by 4, except if it is divisible by 100 but not by 400.

As a programmer, your task is to create a program to help the scientist determine if a year is a leap year.

**Your Task:**
Write a Python function called `is_leap_year(year)` that:

-   Takes a year as input (an integer).
-   Returns `True` if the year is a leap year, `False` otherwise.

**Examples:**

```python
# Example 1
print(is_leap_year(2024))  # Output: True (Divisible by 4 and not a century year)

# Example 2
print(is_leap_year(1900))  # Output: False (Divisible by 100 but not by 400)

# Example 3
print(is_leap_year(2000))  # Output: True (Divisible by 400)

# Example 4
print(is_leap_year(2023))  # Output: False (Not divisible by 4)
```

**Rules:**

1. The input year will always be a positive integer.
2. Your function should correctly handle century years like 1900 and 2000.

Have fun checking for leap years!