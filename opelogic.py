def andfunct(x, y, letterlist):
    if ('!' in x):
        if (x[1] in letterlist): x = '0'
        else: x = '1'
    else:
        if (x in letterlist): x = '1'
        elif x != '0' and x != '1': x = '0'
    if ('!' in y):
        if (y[1] in letterlist): y = '0'
        else: y = '1'
    else:
        if (y in letterlist): y = '1'
        elif y != '0' and y != '1': y = '0'
    # print("x = {}\ny = {}\nx and y = {}".format(x, y, (int(x) and int(y))))
    return (int(x) and int(y))


def orfunct(x, y, letterlist):
    if '!' in x:
        if (x[1] in letterlist): x = '0'
        else: x = '1'
    else:
        if (x in letterlist): x = '1'
        elif x != '0' and x != '1': x = '0'
    if ('!' in y):
        if (y[1] in letterlist): y = '0'
        else: y = '1'
    else:
        if (y in letterlist): y = '1'
        elif y != '0' and y != '1': y = '0'
    # print("x = {}\ny = {}\nx or y = {}".format(x, y, (int(x) or int(y))))
    return (int(x) or int(y))


def xorfunct(x, y, letterlist):
    if ('!' in x):
        if (x[1] in letterlist): x = '0'
        else: x = '1'
    else:
        if (x in letterlist): x = '1'
        elif x != '0' and x != '1': x = '0'
    if ('!' in y):
        if (y[1] in letterlist): y = '0'
        else: y = '1'
    else:
        if (y in letterlist): y = '1'
        elif y != '0' and y != '1': y = '0'
    # print("x = {}\ny = {}\nx xor y = {}".format(x, y, abs(int(x) - int(y))))
    return (abs(int(x) - int(y)))


def letterfunct(x, letterlist):
    if x == '0' or x == '1': return int(x)
    elif '!' in x:
        if x[1] in letterlist: return 0
        else: return 1
    else:
        if x in letterlist: return 1
        else: return 0 