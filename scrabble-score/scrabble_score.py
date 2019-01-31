
#dictionary
def score(word):
    lower_word = word.lower()
    mydict = {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1,
        "l": 1,
        "n": 1,
        "r": 1,
        "s": 1,
        "t": 1,
        "d": 2,
        "g": 2,
        "b": 3,
        "c": 3,
        "m": 3,
        "p": 3,
        "f": 4,
        "h": 4,
        "v": 4,
        "w": 4,
        "y": 4,
        "k": 5,
        "j": 8,
        "x": 8,
        "q": 10,
        "z": 10

    }
    sum = 0
    for letters in lower_word:
        for x, y in mydict.items():
            if letters in x:
                sum = sum + y
    return sum

# other way
def transform(data):
    return {letter.lower(): score
            for score in data
            for letter in data[score]}

score_to_letter = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']}

letter_to_score = transform(score_to_letter)


def score(word):
    return sum([letter_to_score.get(letter, 0)
                for letter in word.lower()])