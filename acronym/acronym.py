def abbreviate(words):
    #some changes
    words = words.replace("-", " ")
    words = words.replace("_", "")
    word_list = words.split()
    for w in word_list:
        if w == " ":
            word_list.remove(w)
    letters = [word[0] for word in word_list]
    acro = ""
    for l in letters:
         l = l.upper()
         acro = acro + l
    return acro