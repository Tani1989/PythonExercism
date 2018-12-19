# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.


def square_of_sum(count):
    index = 1
    total = 0
    result = 0
    while (index <= count):
        total = total + index

        index = index + 1
        result = total ** 2
    return result


# The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

def sum_of_squares(count):
    index = 1
    total = 0

    while (index <= count):
        total = total + index ** 2
        index = index + 1

    return total


def difference(count):
    final_result = square_of_sum(count) - sum_of_squares(count)

    return final_result


# short solution
def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))