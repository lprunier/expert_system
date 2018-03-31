def putletteron(split, i, letterlist):
    # print("i = {}\nlen = {}\n type{}".format(i, len(split), type(letterlist)))
    if i + 1 == len(split) and ("!" in split[i]) == 0:
        if (split[i] in letterlist) == 0: letterlist = letterlist + split[i]
    elif i + 1 == len(split) and ("!" in split[i]) == 1:
        if (split[i][1] in letterlist) == 1: letterlist = letterlist.replace(split[i][1],'')
    print(letterlist)
    return letterlist