# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.
    return sum(range(1, n + 1)) ** 2
# sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))