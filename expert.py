import sys
from opelogic import *
from allfuncts import *
from returnfunct import *

def checkreq(split, begin, end, letterlist):
    # fonction recursive pour checker si la proposition est vraie
    # print("begin = {}\nend = {}".format(begin, end))
    if end - begin < 3:
        if split[begin + 1] == "+": return andfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "|": return orfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "^": return xorfunct(split[begin], split[end], letterlist)
    elif segments(split, begin, end) == 0:
        res = checkreq(split, begin, begin + 2, letterlist)
        split[begin + 2] = str(res)
        return checkreq(split, begin + 2, end, letterlist)
    return 0

def decrypt(request, letterlist):
    split = str.split(request)
    i = 0
    l = len(split)
    while i < l and split[i] != "=>":
        i += 1
    if checkreq(split, 0, i - 1, letterlist):
        print("propal ok")
        return putletteron(split, i + 1, letterlist)
    else:
        print("propal ko")
        return "0"


def main(argv):
    # print("{}".format(argv[0]))
    decrypt(argv[0], argv[1])


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nVoluntary stop")
        sys.exit(1)