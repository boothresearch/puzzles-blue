def count_words(sentence):
    import re 
    sentence=re.sub(r"[!\?\.]", "", sentence )
    sentence=sentence.lower().split()
    wordfreq = [sentence.count(p) for p in sentence]
    return dict(list(zip(sentence,wordfreq)))
