def is_pangram(sentence):

  sentence = sentence.lower()

# for unique letters
  sentence = set(sentence)
# ord(ch) returns ascii value of character
  check = [ch for ch in sentence if ord(ch) in range(ord('a'),ord('z')+1)]
  if len(check) == 26:
    return True
  else:
     return False


# OR
from string import ascii_lowercase

def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)
