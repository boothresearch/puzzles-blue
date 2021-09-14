import math
def score(x, y):
    dist = math.dist([x, y], [0,0])
    if dist > 10:
        return 0
    elif dist == 10:
        return 1
    elif dist <= 10 and dist > 5: 
        return 1
    elif dist <= 5 and dist > 1:
        return 5
    elif dist <= 1:
        return 10
