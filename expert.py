import sys
from opelogic import *
from allfuncts import *

def checkreq(split, begin, end, letterlist):
    # fonction recursive pour checker si la proposition est vraie
    # print("begin = {}\nend = {}".format(begin, end))
    if end - begin < 3:
        #faire cette petite partie de calcul
        if split[begin + 1] == "+": return andfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "|": return orfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "^": return xorfunct(split[begin], split[end], letterlist)
    else: pass
        #couper la requete
    return 1

def decrypt(request, letterlist):
    split = str.split(request)
    i = 0
    l = len(split)
    while i < l and split[i] != "=>":
        i += 1
    if checkreq(split, 0, i - 1, letterlist):
        # print("propal ok")
        # turn on les elements apres l'implication
        # retourne la liste des lettres misent a 1
        return "A"
    else:
        # print("propal ko")
        return "0"


def main(argv):
    # print("{}".format(argv[0]))
    decrypt(argv[0], argv[1])


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nVoluntaru stop")
        sys.exit(1)