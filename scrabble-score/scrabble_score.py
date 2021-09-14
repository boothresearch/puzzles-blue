def score(word):
    list1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    list2 = ["D", "G"]
    list3 = ["B", "C", "M", "P"]
    list4 = ["F", "H", "V", "W", "Y"]
    list5 = ["K"]
    list6 = ["J", "X"]
    list7 = ["Q","Z"]
    all_list = [list1, list2, list3, list4, list5, list6, list7]
    score_dict = {1:1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 8, 7: 10}
    score = 0
    word = str(word.upper())
    for w in word:
        for l in all_list:
            if w in l:
                score += score_dict[all_list.index(l)+1]
    
    return score
