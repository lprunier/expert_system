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


def ope(x):
    if x == '+' or x == '^' or x == '|': return 1
    else: return 0


def char(x):
    if x >= 'A' and x <= 'Z': return 1
    elif len(x) == 2 and x[0] == '!' and x[1] >= 'A' and x[1] <= 'Z': return 1
    else: return 0


def priority(split, begin, end):
    i = begin
    while i <= end:
        if split[i] == '+': return i - 1, i + 1
        i += 1
    i = begin
    while i <= end:
        if split[i] == '|': return i - 1, i + 1
        i += 1
    i = begin
    while i <= end:
        if split[i] == '^': return i - 1, i + 1
        i += 1
    return begin, end
