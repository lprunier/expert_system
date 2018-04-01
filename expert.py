import sys
from opelogic import *
from allfuncts import *
from returnfunct import *


def replacequotes(split, begin, end, letterlist):
    i = 0
    while i <= end and split[i] != ")":
        if split[i] == "(": op = i
        i += 1
    cl = i
    res = checkreq(split, op + 1, cl - 1, letterlist)
    while split[op] != ')':
        del split[op]
    split[op] = str(res)


def checkreq(split, begin, end, letterlist):
    # fonction recursive pour checker si la proposition est vraie
    if end - begin < 3:
        if split[begin + 1] == "+": return andfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "|": return orfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "^": return xorfunct(split[begin], split[end], letterlist)
    elif segments(split, begin, end) == 0:
        res = checkreq(split, begin, begin + 2, letterlist)
        split[begin + 2] = str(res)
        return checkreq(split, begin + 2, end, letterlist)
    else:
        while (segments(split, begin, end) == 1):
            replacequotes(split, begin, end, letterlist)
        end = findend(split) - 1
        return checkreq(split, begin, end, letterlist)
    return 0


def decrypt(request, letterlist):
    split = str.split(request)
    i = findend(split)
    if checkreq(split, 0, i - 1, letterlist):
        # print("propal ok")
        return putletteron(split, findend(split) + 1, letterlist)
    else:
        # print("propal ko")
        return letterlist


def main(argv):
    request = []
    request.append("A | B + C => E")
    request.append("( F | G ) + H => E")
    request.append("A ^ B => C")
    letterlist = "A"
    askletter = "BE"
    printfirstreq(request)
    print("\033[0;4mTrue letters list:\033[0;0m \033[0;1m{}\033[0;0m".format(letterlist))
    print("\033[0;4mAsked letters list:\033[0;0m \033[0;1m{}\033[0;0m\n\n\n\033[0;1mRESOLUTION\033[0;0m\n".format(askletter))
    i = 0
    l = len(request)
    while i < l:
        ret = decrypt(request[i], letterlist)
        if ret != letterlist: 
            letterlist = ret
            printreq(request[i], letterlist)
            # print("\033[0;1m{}\033[0;0m\n".format(letterlist))
            i = -1
        i += 1
    print("\n\033[0;1mRESULTS\033[0;0m\n")
    printres(askletter, letterlist)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nVoluntary stop")
        sys.exit(1)