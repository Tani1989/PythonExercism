# to find a factor of a number
    for i in range(1, number):
        if number % i == 0:
 # range function in python
 The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.

class range(stop)
class range(start, stop[, step])
The arguments to the range constructor must be integers (either built-in int or any object that implements the __index__ special method). If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. If step is zero, ValueError is raised.

For a positive step, the contents of a range r are determined by the formula r[i] = start + step*i where i >= 0 and r[i] < stop.

For a negative step, the contents of the range are still determined by the formula r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.

A range object will be empty if r[0] does not meet the value constraint. Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.

Ranges containing absolute values larger than sys.maxsize are permitted but some features (such as len()) may raise OverflowError.

Range examples:

>>>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append
[1]
[1][2]

Result: [1,2]