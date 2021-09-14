def find_anagrams(word, candidates):
    s = [i.lower() for i in word]
    s.sort()
    return_list = []
    for candidate_word in candidates:
        candidate_word_s = [i.lower() for i in candidate_word]
        candidate_word_s.sort()
        if (s == candidate_word_s) & (word.lower() != candidate_word.lower()):
            return_list.append(candidate_word)
    return(return_list)