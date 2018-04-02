import sys

def putletteron(split, i, letterlist):
    # print("i = {}\nlen = {}\n type{}".format(i, len(split), type(letterlist)))
    if i + 1 == len(split) and ("!" in split[i]) == 0:
        if (split[i] in letterlist) == 0: letterlist = letterlist + split[i]
    elif i + 1 == len(split) and ("!" in split[i]) == 1:
        if (split[i][1] in letterlist) == 1: letterlist = letterlist.replace(split[i][1],'')
    else:
        while i < len(split):
            if ("+" in split[i]) == 1 or ("|" in split[i]) == 1 or ("^" in split[i]) == 1: pass
            elif ("!" in split[i]) == 0 and (split[i] in letterlist) == 0: letterlist = letterlist + split[i]
            elif ("!" in split[i]) == 1 and (split[i][1] in letterlist) == 1: letterlist = letterlist.replace(split[i][1],'')
            i += 1
    return letterlist


def printreq(str, letterlist):
    split = str.split("=>")
    if len(letterlist) == 0:
        print("\033[32;1m'{}' \033[0;0mis true, we will make\033[33;1m '{}'\033[0;0m true.\n".format(split[0].strip(' '), split[1].strip(' ')))
    elif len(letterlist) == 1:
        print("\033[32;1m'{}' \033[0;0mis true, we will make\033[33;1m '{}'\033[0;0m true. So \033[0;1m{}\033[0;0m is true.\n".format(split[0].strip(' '), split[1].strip(' '), letterlist))
    else:
        print("\033[32;1m'{}' \033[0;0mis true, we will make\033[33;1m '{}'\033[0;0m true. So \033[0;1m{}\033[0;0m are true.\n".format(split[0].strip(' '), split[1].strip(' '), letterlist))


def printfirstreq(req):
    i = 0
    l = len(req)
    print("\n\033[0;4mRequests:\033[0m")
    while i < l:
        print("\033[0;1m{}\033[0;0m".format(req[i]))
        i += 1


def printres(askletter, letterlist):
    i = 0
    l = len(askletter)
    while i < l:
        if askletter[i] in letterlist:
            print("\033[32;1m{}\033[0;0m is TRUE.".format(askletter[i]))
        else:
            print("\033[31;1m{}\033[0;0m is FALSE.".format(askletter[i]))
        i += 1
    print("")


def error(str):
    print("\033[31;1mError\033[0;0m : {}".format(str))
    sys.exit(1)