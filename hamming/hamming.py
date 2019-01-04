# def distance(strand_a, strand_b):
# calculate = 0
# for ch1, ch2 in zip(strand_a, strand_b):
# if ch1 != ch2 and len(strand_a) == len(strand_b):
# calculate += 1
# if len(strand_a) != len(strand_b):
# raise ValueError("DNA strands not the same length!")
# return calculate


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands not the same length!")

    calculate = 0
    for index, eachcharacter in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            calculate += 1

    return calculate

print(distance("abcde", "atywi"))

# short
def distance(strand1, strand2):
    return sum(i != j for i, j in zip(strand1, strand2))