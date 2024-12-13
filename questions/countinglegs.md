## Zookeeper's Counting Challenge

**Story:**
A zookeeper is counting the legs of all the animals in one enclosure. There are chickens, goats, and cows. The zookeeper has counted how many of each animal there are, and your job is to calculate the total number of legs.

Each animal has a certain number of legs:

-   Chicken: 2 legs
-   Goat: 4 legs
-   Cow: 4 legs

**Your Task:**
Write a Python function called `total_legs(chickens, goats, cows)` that:

-   Takes three numbers as input: the number of chickens, goats, and cows.
-   Calculates the total number of legs for all the animals.
-   Returns the total number of legs.

**Example:**

```python
# Example 1
print(total_legs(2, 3, 1))  # Output: 18 (2*2 + 3*4 + 1*4)

# Example 2
print(total_legs(0, 0, 0))  # Output: 0

# Example 3
print(total_legs(5, 1, 2))  # Output: 24 (5*2 + 1*4 + 2*4)
```

**Rules:**

1. There will be no negative numbers.
2. The number of animals will always be a positive whole number or zero.

Let's help the zookeeper count all those legs!