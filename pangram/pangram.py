import re
import string
def is_pangram(sentence):
    sentence = sentence.lower()
    sentence1 = re.sub(r'\W*', "", sentence)
    sentence2 = re.sub(r'\d*', "", sentence1)
    sentence3 = re.sub(r'_', "", sentence2)
    character_list = [c for c in string.ascii_lowercase]
    occurence = dict.fromkeys(character_list, 0)
    for char in sentence3:
        occurence[char] += 1
    for val in occurence.values():
        if val == 0:
            return False
    return True
