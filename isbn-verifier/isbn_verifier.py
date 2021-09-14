import re
def is_valid(isbn):
    isbn1 = re.sub(r'-', "", isbn)
    isbn_list = [char for char in isbn1]
    if len(isbn_list) != 10:
        return False
    check_letter = re.findall(r'[A-Z]+', isbn1)
    if len(check_letter) != 0 and check_letter[0] != "X":
        return False
    score = 0
    weight = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(10):
        if isbn1[i].isnumeric():
            score += int(isbn1[i]) * weight[i]
        if isbn1[i] == "X":
            score += 10
    if score % 11 == 0:
        return True
    else:
        return False
