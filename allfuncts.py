def abs(x):
    if x < 0: return -x
    else: return x

def segments(split, begin, end):
    for i in range(begin, end):
        if ("(" in split[i]) == 1 or (")" in split[i]) == 1:
            return 1
    return 0
