def abs(x):
    if x < 0: return -x
    else: return x


def segments(split, begin, end):
    for i in range(begin, end):
        if (i >= len(split)):
            return 0
        if ("(" in split[i]) == 1 or (")" in split[i]) == 1:
            return 1
    return 0


def findend(split):
    i = 0
    l = len(split)
    while i < l and split[i] != "=>":
        i += 1
    return i

