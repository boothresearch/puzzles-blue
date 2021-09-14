def is_isogram(string):
    string0 = string.replace(" ","").replace("-","")
    string0 = string0.lower()
    if len(set(string0)) == len(string0):
        return True
    else:
        return False
