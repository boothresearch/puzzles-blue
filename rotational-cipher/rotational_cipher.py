def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    plain = [i for i in plain]
    rotated = plain[key:] + plain[:key]
    plain_upper = [i.upper() for i in plain]
    plain_upper = [i for i in plain_upper]
    rotated_upper = plain_upper[key:] + plain_upper[:key]
    dict_letter = dict(zip(plain+plain_upper, rotated+rotated_upper))
    newtext = ""
    for i in text:
        if i in plain+plain_upper:
            newtext += dict_letter[i]
        else:
            newtext += i
    return newtext
